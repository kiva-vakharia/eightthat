

beaches = {
    'The Wedge': '5842041f4e65fad6a770882b', 
    'Corona Del Mar': '5842041f4e65fad6a77088f3', 
    'Newport Point': '5842041f4e65fad6a77088f2', 
    'Blackies': '584204204e65fad6a7709115',
    'Newport Lower Jetties': '5842041f4e65fad6a770882a',
    'Crystal Cove': '5842041f4e65fad6a7708f21',
    'Newport Upper Jetties': '5842041f4e65fad6a7708e54',
    'River Jetties': '5842041f4e65fad6a77088ee',
    'Crescent Bay': '640a3f7ae92030a2449dd23c',
    'Rockpile': '5842041f4e65fad6a77088e3',
    'Huntington State Beach': '584204204e65fad6a770998c',
    'Thalia Street': '5842041f4e65fad6a77088de',
    'Brooks Street': '5842041f4e65fad6a77088dd',
    'Huntington St.': '58bdebbc82d034001252e3d2',
    'Agate Street': '640a3f794eb37508e5945334',
    'Huntington Beach Pier Southside': '5842041f4e65fad6a77088ed',
    'North HB': '5842041f4e65fad6a77088ea',
    'Aliso Creek': '5842041f4e65fad6a77088dc',
    'HB Cliffs': '640a3f7c606c45fdf1b09880'
     }

def get_beach_id(name_beach):
    return beaches[name_beach]
    
def list_beaches():
    all_beaches = list(beaches.keys())
    return all_beaches
