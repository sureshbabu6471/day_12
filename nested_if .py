TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["TEMPLATE_DIR",],
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
#in the given list if fist element is dic then find out context_processers  value that value is list then find out the 3 rd element is string then print suresh
#otherwise print sathish
#if first element is not dic then print we can not any thing"

print(type(TEMPLATES))
print(type(TEMPLATES[1==0=='string']))
a=['context_processors'[3][0]]
print(type(a))
if TEMPLATES :
    if ['context_processors'[3][0]]:
        print("SURESH")
    elif TEMPLATES:
        print("sathish")
else:
    print("we can not any thing")   