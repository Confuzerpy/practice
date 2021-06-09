if __name__ == '__main__':
    global_init(input())
    session = create_session()
    for job in session.query(Jobs).filter(Jobs.work_size < 20, ~Jobs.is_finished):
        print(job)
