from segno import helpers

qrcode = helpers.make_vcard(name='Last-Name; First-Name', displayname='First-Name Last-Name',
                            org='Minions.app',
                            title='CTO',
                            email='oneinaminion@minions.app',
                            phone=['+852 12345678', '+852 12345678'],
                            fax='+852 12345678',
                            url=['www.microsoft.com/zh-hk', 'azure.microsoft.com/en-us'],
                            street='15/F, Cyberport 2, 100 Cyberport Road',
                            city='Hong Kong')
qrcode.save('my-vcard.svg', scale=5)