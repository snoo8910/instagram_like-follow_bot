from instapy import InstaPy

session = InstaPy(username = '3baprinting', password = 'poggers123')
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

session.set_do_follow(True, percentage=100)
session.like_by_tags(["3d printing", "animation"])

session.end()
