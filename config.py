# Copyright ©️ 2023 Sanila Ranatunga. All Rights Reserved

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 29452145)
    API_HASH = os.environ.get("API_HASH","5a2784e571fe5043852d32396a34a13b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7445547849:AAHfX4_8TQ57cg71Q_l9ABoa6RfgfPWHgsE")
