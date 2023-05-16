import base64
import time
import rsa


def rsa_encrypt(msg, server_pub_key):
    """
    rsa加密
    :param msg: 待加密的数据
    :param server_pub_key: pem格式的服务端公钥
    """

    # 生成公钥对象
    # 转换为字节类型
    pub_key_byte = server_pub_key.encode()
    pub_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key_byte)
    # 要加密的数据转换为字节对象
    content = msg.encode('utf-8')
    # 加密，返回加密文本
    crypt_msg = rsa.encrypt(content, pub_key_obj)
    # 把加密后的密文转换为base64格式的字符串
    res = base64.b64encode(crypt_msg).decode()
    return res


def generate_sign(token, pub_key):
    """
    生成签名
    :param token: token
    :param pub_key: pem格式的公钥
    :return:
    """
    # 获取token的前50位
    token_50 = token[:50]
    # 获取当前时间戳
    timestamp = int(time.time())
    # 拼接token和时间戳
    msg = token_50 + str(timestamp)
    # rsa加密
    sign = rsa_encrypt(msg, pub_key)
    return sign, timestamp
