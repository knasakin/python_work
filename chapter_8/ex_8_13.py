# 8.13. Профиль
def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile_1 = build_profile('albert', 'einstein', location='princeton', field='physics')
user_profile_2 = build_profile('konstantin', 'nasakin', location='volzhskiy', field='programming')
print(user_profile_1)
print(user_profile_2)
