from django.core.mail.backends.smtp import EmailBackend
import ssl
import certifi


class CustomEmailBackend(EmailBackend):
    def _get_ssl_context(self):
        return ssl.create_default_context(cafile=certifi.where())

    def open(self):
        # If the connection is already open, do nothing.
        if self.connection:
            return False
        try:
            if hasattr(self, 'connection_params') and self.connection_params:
                self.connection = self.connection_class(
                    self.host,
                    self.port,
                    timeout=self.timeout,
                    **self.connection_params
                )
            else:
                self.connection = self.connection_class(
                    self.host,
                    self.port,
                    timeout=self.timeout
                )

            self.connection.set_debuglevel(self.use_tls and self.ssl_debuglevel)
            self.connection.ehlo()
            if self.use_tls:
                self.connection.starttls(context=self._get_ssl_context())
                self.connection.ehlo()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except:
            if self.fail_silently:
                return False
            raise
