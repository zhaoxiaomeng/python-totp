class TOTP:
    secret = ''
    period = None
    skew = None
    digits = None
    algorithm = None

    # Server generate new TOTP key for new user
    def generate(self, user_option):
        return
    # Client generate new code
    def generate_code(self):
        return

    # Server validate client code
    def validate_code(self, code):
        return

    def __init__(self, period, skew, digits, algorithm):
        self.period = period
        self.skew = skew
        self.digits = digits
        self.algorithm = algorithm
        return
