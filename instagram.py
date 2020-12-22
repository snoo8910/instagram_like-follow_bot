from instapy import InstaPy

session = InstaPy(username = 'ENTER_USERNAME', password = 'ENTER_PASSWORD')
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

session.set_do_follow(True, percentage=100)
session.like_by_tags(["INTSERT_TAG"])

session.end()
