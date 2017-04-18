import secrets

MESSAGE_LEN = 140


def gen_otp():
    """
    :return: a list of random integers of length MESSAGE_LEN to be used as a one time pad
    """
    return [secrets.randbelow(95) * MESSAGE_LEN]


def format_text(text):
    """
    :param text: a string containing ASCII characters inputted by the user
    :return: a list of integers representing characters to be encrypted/decrypted
    :raise: ValueError if message is too long or contains non-ASCII characters
    :raise: UnicodeDecodeError if message is non-ASCII
    """
    if len(text) > MESSAGE_LEN:
        raise ValueError("Message exceeds maximum message length")

    try:
        text.encode('ascii')
    except UnicodeDecodeError:
        raise

    # handle tabs?

    text += ' '*(MESSAGE_LEN - len(text))
    return [ord(ch)-ord(' ') for ch in text]


def encrypt(message, otp):
    """
    :param message: an ASCII string to be encrypted
    :param otp: a one time pad
    :return: an encrypted ASCII string
    """
    message = format_text(message)
    return ''.join(
        chr(((m_ch + otp_ch) % 95) + ord(' '))
        for m_ch, otp_ch in zip(message, otp)
    )


def decrypt(code, otp):
    """
    :param code: an ASCII string to be decrypted
    :param otp: the one time pad used to encrypt the code. result will be nonsense if the incorrect OTP is used
    :return: the message--the decrypted ASCII string
    """
    code = format_text(code)
    return ''.join(
        chr(((c_ch - otp_ch) % 95) + ord(' '))
        for c_ch, otp_ch in zip(code, otp)
    )






