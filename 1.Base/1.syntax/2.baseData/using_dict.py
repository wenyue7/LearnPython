#!/usr/bin/python
# Filename: using_dict.py

# 'm_dic' is short for 'a'ddress'b'ook
m_dic = {'Swaroop' : 'swaroopch@byteofpython.info',
        'Larry' : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer' : 'spammer@hotmail.com'}
print("Swaroop's address is %s" % m_dic['Swaroop'])
# Adding a key/value pair
m_dic['Guido'] = 'guido@python.org'
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组
m_dic[(10, 14)] = 'test@python.org'
# Deleting a key/value pair
del m_dic['Spammer']
print('\nThere are %d contacts in the address-book\n' % len(m_dic))
for name, address in m_dic.items():
    print('Contact %s at %s' % (name, address))
if 'Guido' in m_dic: # OR m_dic.has_key('Guido')
    print("\nGuido's address is %s" % m_dic['Guido'])

m_dic.clear()
print('\nThere are %d contacts in the address-book\n' % len(m_dic))
