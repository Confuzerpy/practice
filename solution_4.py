if __name__ == '__main__':
    global_init(input())
    session = create_session()
    for user in session.query(User).filter(User.age < 21, User.address == 'module_1'):
        user.address = 'module_3'
    session.commit()
