SECRET_KEY = ')na6im8wvqqq7uza+57wx#sef5((kj%@102#+wy7$5#x)i3z$l'

import simpleui
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

import time

###
# SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
# SIMPLEUI_HOME_TITLE = '智慧畜牧系统'
# SIMPLEUI_HOME_ICON = 'fa fa-user'
SIMPLEUI_ANALYSIS = False
SIMPLEUI_DEFAULT_THEME = 'highdmin.css'
#SESSION_COOKIE_AGE=60*10
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SIMPLEUI_HOME_INFO = False

SIMPLEUI_CONFIG = {
    'system_keep': True,
    'menu_display': ['用户管理', '基本管理', '圈舍管理', '卫生管理', '繁育管理', '饲养管理', '屠宰销售管理', '库存管理', '供应管理', '数据统计及报表管理'],
    # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': True,  # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [
        # {
        # 'app': 'account',
        # 'name': '用户管理',
        # 'icon': 'fas fa-user-shield',
        # 'url': 'account/myuser/'

        # },
        {
            'app': 'app1',
            'name': '基本管理',
            'icon': 'fa fa-database',
            'models': [{
                'name': '羊只基本信息',
                'icon': 'fa fa-database',
                'url': 'http://127.0.0.1:8888/sheep/manage/admina_sheep.jsp'
            }, {
                'name': '羊只产地信息',
                'icon': 'fa fa-database',
                'url': 'basic/manuinfo/'
            }, {
                'name': '种羊体况',
                'icon': 'fa fa-database',
                'url': 'basic/breederconditioninfo/'
            }, {
                'name': '剪毛信息',
                'icon': 'fa fa-database',
                'url': 'basic/cutinfo/'
            }, {
                'name': '运动数据',
                'icon': 'fa fa-database',
                'url': 'basic/sportsinfo/'
            }, {
                'name': '泌乳性能',
                'icon': 'fa fa-database',
                'url': 'basic/milkperformance/'
            }, {
                'name': '产皮性能',
                'icon': 'fa fa-database',
                'url': 'basic/skinperformance/'
            }
            ]
        }, {
            'name': '圈舍管理',
            'icon': 'fa fa-map-signs',
            'models': [{
                'name': '棚舍管理',
                'url': 'http://127.0.0.1:8888/sheep/manage/admina_houseinfo.jsp',
                'icon': 'fa fa-map-signs'
            }, {
                'name': '栏舍管理',
                'url': 'http://127.0.0.1:8888/sheep/manage/admina_houseinfoColumn.jsp',
                'icon': 'fa fa-map-signs'
            }, {
                'name': '圈舍消毒信息',
                'url': 'colony/disinfectioninfo',
                'icon': 'fa fa-map-signs'
            }]
        }, {
            'name': '卫生管理',
            'icon': 'fa fa-medkit',
            'models': [{
                'name': '接种免疫表',
                'url': 'd_health/immunizationinfo/',
                'icon': 'fa fa-medkit'
            }, {
                'name': '药浴消毒',
                'url': 'd_health/drugbathinfo/',
                'icon': 'fa fa-medkit'
            }, {
                'name': '检疫检验',
                'url': 'd_health/quarantineinfo/',
                'icon': 'fa fa-medkit'
            }, {
                'name': '护理信息',
                'url': 'd_health/nursinginfo/',
                'icon': 'fa fa-medkit'
            }, {
                'name': '疾病信息',
                'url': 'd_health/diseaseinfo/',
                'icon': 'fa fa-medkit'
            }, {
                'name': '死亡信息',
                'url': 'd_health/deathinfo/',
                'icon': 'fa fa-medkit'
            }
            ]
        }, {
            'name': '繁育管理',
            'icon': 'fa fa-heart',
            'models': [
                {
                    'name': '发情信息',
                    'icon': 'fa fa-heart',
                    'url': 'e_breed/rutinfo',
                }, {
                    'name': '采精信息',
                    'icon': 'fa fa-heart',
                    'url': 'e_breed/semencollectinfo',
                }, {
                    'name': '配种信息',
                    'icon': 'fa fa-heart',
                    'url': 'e_breed/breedinginfo',
                }, {
                    'name': '孕期检测',
                    'icon': 'fa fa-heart',
                    'url': 'e_breed/pregnantinfo',
                }, {
                    'name': '产后信息',
                    'icon': 'fa fa-heart',
                    'url': 'e_breed/postnatalinfo',
                }, {
                    'name': '人工喂养',
                    'icon': 'fa fa-heart',
                    'url': 'e_breed/artificialfeedinginfo',
                }, {
                    'name': '断奶信息',
                    'icon': 'fa fa-heart',
                    'url': 'e_breed/weaninginfo',
                },
                {
                    'name': '羔羊信息',
                    'icon': 'fa fa-heart',
                    'url': 'e_breed/lambinfo',
                },
                {
                    'name': '导出配种所有信息',
                    'icon': 'fa fa-heart',
                    'url': 'e_breed/export_breed',
                }
            ]
        }, {
            'name': '饲养管理',
            'icon': 'fa fa-bars',
            'models': [
                {
                    'name': '饲养管理信息',
                    'icon': 'fa fa-bars',
                    'url': ''
                }, {
                    'name': '饲养管理系统',
                    'icon': 'fa fa-bars',
                    'url': ''
                }
                ,
                {
                    'name':'圈舍喂养信息',
                    'icon':'fa fa-bars',
                    'url':'feeding/feedhouseinfo'
                }
            ]
        }, {
            'name': '屠宰销售管理',
            'icon': 'fa fa-truck',
            'models': [
                {
                    'name': '羊只销售',
                    'icon': 'fa fa-truck',
                    'url': 'g_slaughter/s_salesinfo'
                }, {
                    'name': '羊副产品销售',
                    'icon': 'fa fa-truck',
                    'url': 'g_slaughter/g_salesinfo'
                }, {
                    'name': '经济效益',
                    'icon': 'fa fa-truck',
                    'url': 'g_slaughter/economicinfo'
                }, {
                    'name': '屠宰分割 ',
                    'icon': 'fa fa-truck',
                    'url': 'g_slaughter/slaughtersegmentinfo'
                }, {
                    'name': '膘情B超',
                    'icon': 'fa fa-truck',
                    'url': 'g_slaughter/binformationinfo'
                }
            ]
        }, {
            'name': '库存管理',
            'icon': 'fa fa-warehouse',
            'models': [
                {
                    'name': '物资库存信息',
                    'icon': 'fa fa-warehouse',
                    'url': 'h_store/inventory/'
                }, {
                    'name': '疫苗&药品入库信息',
                    'icon': 'fa fa-warehouse',
                    'url': 'h_store/vaccine_in/'
                }, {
                    'name': '疫苗&药品出库信息',
                    'icon': 'fa fa-warehouse',
                    'url': 'h_store/vaccine_out/'
                }, {
                    'name': '饲料入库信息',
                    'icon': 'fa fa-warehouse',
                    'url': 'h_store/feedingin/'
                }, {
                    'name': '饲料出库信息',
                    'icon': 'fa fa-warehouse',
                    'url': 'h_store/feeding_out/'
                }
            ]
        }, {
            'name': '供应管理',
            'icon': 'fa fa-code-branch',
            'models': [
                {
                    'name': '疫苗厂商信息',
                    'icon': 'fa fa-code-branch',
                    'url': 'supply/v_suppliersinfo/'
                },
                {
                    'name': '饲料厂商信息',
                    'icon': 'fa fa-code-branch',
                    'url': 'supply/f_suppliersinfo/'
                },
                {
                    'name': '保险公司信息',
                    'icon': 'fa fa-code-branch',
                    'url': 'supply/insuranceinfo/'
                },
                {
                    'name': '疫苗药品信息',
                    'icon': 'fa fa-code-branch',
                    'url': 'supply/commodityinfo/'
                }
            ]
        }, {
            'name': '数据统计及报表管理',
            'icon': 'fa fa-chart-pie',
            'models': [
                {
                    'name': '淘汰羊只',
                    'icon': 'fa fa-chart-pie',
                    'url': 'http://39.99.175.254:8888/sheep/manage/admina_sheepAll.jsp'
                },
                {
                    'name': '系谱档案',
                    'icon': 'fa fa-chart-pie',
                    'url': 'basic/basicinfo/'
                },
                {
                    'name': '数据统计(自动生成)',
                    'icon': 'fa fa-chart-pie',
                    'url': ''
                }, {
                    'name': '日报表',
                    'icon': 'fa fa-chart-pie',
                    'url': ''
                }, {
                    'name': '年度报表数据(自动生成)',
                    'icon': 'fa fa-chart-pie',
                    'url': ''
                }, {
                    'name': '生产性能详细',
                    'icon': 'fa fa-database',
                    'url': 'basic/productivityinfo/'
                }
            ]
        },
    ]
}

###


# SECRET_KEY = ')na6im8wvqqq7uza+57wx#sef5((kj%@102#+wy7$5#x)i3z$l'


DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.account',
    'apps.basic',
    'apps.colony',
    'apps.d_health',
    'apps.e_breed',
    'apps.feeding',
    'apps.g_slaughter',
    'apps.h_store',
    'apps.supply',
    'apps.home',
    'import_export'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'simpleui_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

WSGI_APPLICATION = 'simpleui_test.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sheep',
        'USER': 'root',
        'PASSWORD': 'unclered123.',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
            'charset': 'utf8mb4'
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

#USE_TZ = True

#user
AUTH_USER_MODEL = 'account.MyUser'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

#路由
STATIC_URL = '/static/'

#收集静态的位置
STATIC_ROOT = os.path.join(BASE_DIR, "collect_static")

#目录
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

if DEBUG == True:
    INTERNAL_IPS = ['*']
    INSTALLED_APPS.append('debug_toolbar')
    DEBUG_TOOLBAR_CONFIG = {
        # 'JQUERY_URL': '//cdn.bootcss.com/jquery/2.1.4/jquery.min.js',
        # 或把jquery下载到本地然后取消下面这句的注释, 并把上面那句删除或注释掉
        'JQUERY_URL': '/static/js/jquery-3.4.1.min.js',
        'SHOW_COLLAPSED': True,
        'SHOW_TOOLBAR_CALLBACK': lambda x: True,
    }
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.history.HistoryPanel',
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
    ]