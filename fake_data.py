import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tracertly.settings')

import django
django.setup()

from django.utils import timezone

from boards.models import (
    Board,
    Listing,
    Item,
    Comment,
    Milestone,
)

from divisions.models import (
    Team,
    Section
)

from users.models import UserProfile
from django.contrib.auth.models import User

#  Create an Example Board
class Tracertly_Faker():
    board_name = "Example Board: Going Social"
    board_description = "As the Marketing Department. We are planning to go social and this is the platform for brainstorming all our ideas."

    def __init__(self):
        board = self.add_listings()

    def create_user(self):
        user_name = "johndoe"
        user, created = User.objects.get_or_create(username=user_name)
        user.save()
        return user
    
    def create_section(self):
        fake_user           = self.create_user()
        section_name = 'Marketing'
        section_descrition = "The Marketing Section in short deals with getting the product in front of the customer etc .."
        section, created = Section.objects.get_or_create(
            name=section_name, 
            description=section_descrition,
            creator         = fake_user,
            )

        section.save()
        return section

    def create_board(self):
        fake_user           = self.create_user()
        fake_section        = self.create_section()
        board, created               = Board.objects.get_or_create(
            name            = self.board_name,
            description     = self.board_description,
            creator         = fake_user,
            section         = fake_section,
            public          = True
            )
        board.save() 
        return board

    def add_listings(self):
        fake_user = self.create_user()
        fake_board = self.create_board()
        listings = {
            1:{
               'name': "Marketing Campaigns",
               'description': "What Campaigns are we going to use to achieve this goal"
            },
            2:{
               'name': "Social Media",
               'description': "What Social Media Platforms are we going to use"
            }
        }
        for key, listing in listings.items():
            fake_listing = Listing.objects.get_or_create(
                    name=listing['name'],
                    description=listing['description'],
                    board=fake_board,
                    creator=fake_user
                )
            fake_listing[0].save()
            # for eack fake listing add items
            if fake_listing[0].name == "Social Media":
                social_items = {
                    1:{
                    'name': "FaceBook",
                    'description': "With Facebook we can target very Large Audiences for friends and families across all age groups"
                    },
                    2:{
                    'name': "Twitter",
                    'description': "Short descriptive messages that can go viral"
                    },
                    3:{
                    'name': "Instagram",
                    'description': "Graphics Driven social media markerting"
                    },
                    4:{
                    'name': "SnapChat",
                    'description': "Mainly for targetiing the youth. Youths are heavily migrating from FB to SC"
                    }
                }
                for key, item in social_items.items():
                    # assign twitter or snapchat to fake_user
                    if item['name'] == "Twitter" or item['name'] == "SnapChat":
                        fake_item = Item.objects.get_or_create(
                            name = item['name'],
                            description = item['description'],
                            Listing = fake_listing[0],
                            creator = fake_user,
                            assignee = fake_user
                        )
                    else:
                        fake_item = Item.objects.get_or_create(
                            name = item['name'],
                            description = item['description'],
                            creator = fake_user,
                            Listing = fake_listing[0]
                        )
                    fake_item[0].save()
                    # create milestones, comments etc 

    


if __name__ == '__main__':

    print("\nInitializing Fake Data Creation \n")
    Tracertly_Faker()
    print("Fake Data Creation Done!")
