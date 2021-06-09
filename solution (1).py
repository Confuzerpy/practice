if __name__ == '__main__':

    hours = {}
    global_init(input())
    session = create_session()

    for job in session.query(Jobs).all():
        time = job.work_size if job.is_finished else \
            min((datetime.datetime(year=2021, month=4, day=27) -
                 job.start_date).seconds // 3600, job.work_size)
        hours[job.team_leader] = hours.get(job.team_leader, 0) + time

        for user_id in map(int, job.collaborators.split(', ')):
            hours[user_id] = hours.get(user_id, 0) + time

    for user_id in map(int, session.query(Department).first().members.split(', ')):
        user = session.query(User).filter(User.id == user_id).first()
        if user_id in hours and hours[user_id] > 25:
            print(user.surname, user.name)
