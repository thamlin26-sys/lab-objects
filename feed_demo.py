"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    # Create your accounts and posts, then call their methods.
    # Return the two lists: return users, posts
    pass
    user1 = User("hoops_fanatic")
    user2 = User("court_vision")

    tweet1 = Tweet("hoops_fanatic", "What an incredible buzzer beater! #GameWinner #NBA")
    tweet2 = Tweet("court_vision", "Great team defense tonight. #Lockdown")
    tweet3 = Tweet("hoops_fanatic", "Time to review the game film tomorrow.")
    
    user1.follow()
    user1.follow()
    user1.unfollow()
    
    tweet1.like()
    tweet1.like()
    tweet1.unlike()
    
    users = [user1, user2]
    posts = [tweet1, tweet2, tweet3]
    return users, posts


def main():
    # Call build_feed and display the returned objects and hashtags.
    pass
    users, posts = build_feed()
    
    print("Basketball Community Users")
    for user in users:
        print(user)
        
    print("Basketball Community Posts & Hashtags")
    for post in posts:
        print(post)
        tags = post.hashtags()
        if tags:
            print(f"Hashtags: {tags}")


if __name__ == '__main__':
    main()
