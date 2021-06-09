if __name__ == '__main__':
    global_init(input())
    session = create_session()
    counts = {}
    for job in session.query(Jobs).all():
        count = len(job.collaborators.split(', '))
        counts[count] = counts.get(count, [])
        counts[count].append(job.team_leader)
    for user in session.query(User).filter(User.id.in_(counts[max(counts)])):
        print(user.surname, user.name)
