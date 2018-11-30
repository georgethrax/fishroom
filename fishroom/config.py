config = {
    "debug": True,
    "timezone": "Asia/Shanghai",
    "baseurl": "http://52.68.175.168:8000",  # do not end with "/"
    "name": "ivision",
    "cmd_me": "tg_bot",  # username of the telegram bot

    "redis": {
        # "unix_socket_path": "/var/run/redis/redis.sock"
        "host": "localhost",  # hostname for redis server
        "port": 6379,
        "prefix": "fishroom",
    },

    "irc": {
        "server": "irc.freenode.net",
        "port": 6697,
        "nick": "XiaoT",       # IRC nick name
        "password": None,      # IRC account password, if nickname registered
        "ssl": True,
        "blacklist": [
            "[Olaf]",
        ],
    },

    # Uncomment these if you want telegram access
    # "telegram": {
    #     "token": "",  # get this from @BotFather
    #     "me": None,
    #     "admin": [],  # admin id (integer)
    # },

    # Uncomment these if you want XMPP-MUC access
    # "xmpp": {
    #     "server": "xmpp.jp",
    #     "port": 5222,
    #     "jid": "user@xmpp.jp/resource",
    #     "password": "",
    #     "nick": "XiaoT",
    # },

    # Uncomment these if you want gitter access
    # "gitter": {
    #     "token": "",
    #     "me": "",  # bot username
    # },

    # Uncomment these if you want Matrix access
    # "matrix": {
    #     "server": "https://matrixim.cc:8448",
    #     "user": "fishroom",
    #     "password": "",
    #     "nick": "bot_fishroom",
    #     "bot_msg_pattern": "^mubot|^!wikipedia",
    # },

    # Uncomment these if you want WeChat access
    # "wechat": {},

    # Optional, only if you use qiniu for file_store
    # Comment this out if you don"t use qiniu
    #"qiniu": {
    #    "access_key": "",
    #    "secret_key": "",
    #    "bucket": "",
    #    "base_url": "",
    #},

    #"photo_store": {
        # set one in ("imgur", "vim-cn", "qiniu")
    #    "provider": "vim-cn",
    #    "options": {
    #        "client_id": "",
    #    }
    #},

    # this is the web interface
    "chatlog": {
        "host": "52.68.175.168",  # hostname for web server
        "port": 8000,
        "default_channel": "ivision",
    },

    # Comment this out if you don"t use qiniu
    #"file_store": {
    #    "provider": "qiniu",
    #},

    "text_store": {
        "provider": "redis",
        "options": {
        },
    },

    "plugins": [
        "pia", "imglink", "vote", "hualao"
    ],

    "bindings": {
        "archlinux-cn": {
            "irc": "#archlinux-cn",
            "telegram": "-1001031857103",  # group id can be obtained using bot api
            "xmpp": "chat@conference.xmpp.jp",
            "matrix": "#archlinux:matrixim.cc"
        },
        "test": {
            # Use room nick name to identify a room
            # TODO: use Uins (https://itchat.readthedocs.io/zh/latest/intro/contact/#uins)
            # to identify a room, but currently I can"t get room Uins on login.
            "wechat": "xxx chat room"
        },
	"ivision":{
	}
    }
}

# vim: ft=python
