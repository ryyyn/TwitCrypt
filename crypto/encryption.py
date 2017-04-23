import secrets

MESSAGE_LEN = 140


def gen_otp():
    """
    :return: a string of comma delimited random integers of length MESSAGE_LEN 
             to be used as a one time pad and for storage in the database
    """
    return ','.join(str(secrets.randbelow(94)) for n in range(MESSAGE_LEN))


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
    return [ord(ch)-ord(' ') for ch in text]


def encrypt(message, otp):
    """
    :param message: an ASCII string to be encrypted
    :param otp: an ASCII string that represents a one time pad
    :return: an encrypted ASCII string
    """
    formatted = format_text(message)
    otp = [int(n) for n in otp.split(',')]

    return ''.join(
        chr(((m_ch + otp_ch) % 94) + ord('!'))
        for m_ch, otp_ch in zip(formatted, otp)
    )


def decrypt(code, otp):
    """
    :param code: an ASCII string to be decrypted
    :param otp: the one time pad used to encrypt the code. result will be nonsense if the incorrect OTP is used
    :return: the message--the decrypted ASCII string
    """
    code_arr = [ord(ch)-ord('!') for ch in code]
    otp = [int(n) for n in otp.split(',')]

    return ''.join(
        chr(((c - o) % 94) + ord(' '))
        for c, o in zip(code_arr, otp)
    )
