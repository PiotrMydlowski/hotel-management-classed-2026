"""
By PM 2026
Based on web tutorial.
Demonstrates classes using simple hotels management with sorting.
===========
"""


class Hotel :
    sortParam='name'
    def __init__(self) -> None:
        self.name=''
        self.roomAvl=0
        self.location=''
        self.rating=int
        self.pricePr=0
    
    def __lt__(self,other): #Dunder method defining the < sign
        # It also replaces the need for key attribute when sorting with sort()
        getattr(self,Hotel.sortParam)<getattr(other,Hotel.sortParam)
    
    @classmethod
    def sortByName(cls): # Function to change sort parameter to name
        cls.sortParam='name'

    @classmethod
    def sortByRate(cls): # Function to change sort parameter to rating
        cls.sortParam='rating'

    @classmethod
    def sortByRoomAvailable(cls): # Function to change sort parameter to room availability
        cls.sortParam='roomAvl'
    
    def __repr__(self) -> str: # Dunder method creating output for printing
        return "Hotel Name: {}\tRoom Available: {}\tLocation: {}\tRating: {}\tPrice Per Room: {}".format(self.name,self.roomAvl,self.location,self.rating,self.pricePr)


class User:
    def __init__(self) -> None:
        self.uname=''
        self.uId=0
        self.cost=0

    def __repr__(self) -> str: # Dunder method creating output for printing
        return "UserName:{}\tUserId:{}\tBooking Cost:{}".format(self.uname,self.uId,self.cost)


def PrintHotelData(hotels):
    # Print hotels data
    print('---Printing hotels data---')
    for h in hotels:
        print(h)
    print('---End---')


# Sort Hotels data by name.
def SortHotelByName(hotels):
    print("SORT BY NAME:")

    Hotel.sortByName()
    hotels.sort()

    PrintHotelData(hotels)
    print()


# Sort Hotels by rating
def SortHotelByRating(hotels):
    print("SORT BY A RATING:")

    Hotel.sortByRate()
    hotels.sort()
    
    PrintHotelData(hotels)
    print()


# Print Hotels for any city Location.
def PrintHotelBycity(s,hotels):
    print("HOTELS FOR {} LOCATION ARE:".format(s))
    hotelsByLoc=[h for h in hotels if h.location==s]
    
    PrintHotelData(hotelsByLoc)
    print()



# Sort hotels by room Available.
def SortByRoomAvailable(hotels):
    print("SORT BY ROOM AVAILABLE:")
    Hotel.sortByRoomAvailable()
    hotels.sort()
    PrintHotelData(hotels)
    print()


# Print the user's data
def PrintUserData(userName, userId, bookingCost, hotels):
    users=[]
    # Access user data.
    for i in range(3) :
        u=User()
        u.uname = userName[i]
        u.uId = userId[i]
        u.cost = bookingCost[i]
        users.append(u)

    for i in range(len(users)) :
        print(users[i],"\tHotel name:",hotels[i].name)
    


# Functiont to solve
# Hotel Management problem
def HotelManagement(userName,
                     userId,
                     hotelName,
                     bookingCost,
                     rooms,
                     locations,
                     ratings,
                     prices):
    # Initialize arrays that stores
    # hotel data and user data
    hotels=[]

    # Create Objects for
    # hotel and user.

    # Initialise the data
    for i in range(3) :
        h=Hotel()
        h.name = hotelName[i]
        h.roomAvl = rooms[i]
        h.location = locations[i]
        h.rating = ratings[i]
        h.pricePr = prices[i]
        hotels.append(h)
    
    print()

    # Call the various operations
    PrintHotelData(hotels)
    SortHotelByName(hotels)
    SortHotelByRating(hotels)
    PrintHotelBycity("L1",
                     hotels)
    SortByRoomAvailable(hotels)
    PrintUserData(userName,
                  userId,
                  bookingCost,
                  hotels)


def main():
    # Main function

    # Initialize hotels data and user data
    userName = ["U1", "U2", "U3"]
    userId = [2, 3, 4] 
    hotelName = ["H1", "H2", "H3"] 
    bookingCost = [1000, 1200, 1100]
    rooms = [4, 5, 6] 
    locations = ["L1", "L2", "L3"]
    ratings = [5, 5, 3]
    prices = [100, 200, 100] 

    # Function to perform operations
    HotelManagement(userName, userId,
                    hotelName, bookingCost,
                    rooms, locations,
                    ratings, prices)

    print('Finished.')
    

if __name__ == "__main__":
    main()
    