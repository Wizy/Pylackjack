import random

players_hand = []
dealers_hand = []
bankroll = 500
bet = 0
shoe = []
sorted_decks = []
playing = False
for x in range(0,4): #Create sorted stack of 4 decks
    for suit in ["Spades","Diamonds","Clubs","Hearts"]:
        for face_value in range(2,12):
            sorted_decks.append({"suit":suit,"number":face_value})
        for face_value in range(0,3):
            sorted_decks.append({"suit":suit,"number":10})

def shuffle_up():
    print("SHUFFLE UP!")
#    temp_deck = sorted_decks.copy()
#    for x in range(0, len(sorted_decks)):
#        selected_card = random.choice(temp_deck)
#        shoe.append(selected_card)
#        temp_deck.remove(selected_card)
    global shoe 
    shoe = sorted_decks.copy()
    random.shuffle(shoe)

def deal_out():
    #simulate real deal out, I know it's unnecessary
    global shoe
    players_hand.append(shoe.pop())
    dealers_hand.append(shoe.pop())
    players_hand.append(shoe.pop())
    print(players_hand)
    print(dealers_hand)
    print(calc_hand(players_hand))
    if calc_hand(players_hand) == 21:
        game_over()

def calc_hand(hand, is_dealer = False):
    total = 0
    index_of_aces = []
    for card in hand:
        total+=card["number"]
        if card["number"] == 11:
            index_of_aces.append(hand.index(card))

    if is_dealer and total < 18 and len(index_of_aces) > 0: #Dealer hits on soft 17 and less, so calculate as lesser value
        hand[index_of_aces.pop()] = 1
        total = total - 10
    elif total > 21 and len(index_of_aces) > 0: #Player can hit on any soft value
        hand[index_of_aces.pop()] = 1
        total = total - 10

    return total

def game_over():
    global playing
    player_total = calc_hand(players_hand)
    dealer_total = calc_hand(dealers_hand)
    #Blackjack outcomes
    if player_total == 21 and len(players_hand) == 2:
        print("You have blackjack, you win!")
    elif dealer_total == 21 and len(dealers_hand) == 2:
        print("The dealer has blackjack, you lose!")
    #Busted hand outcomes
    elif player_total > 21:
        print("You busted. You lose!")
    elif dealer_total > 21:
        print("The dealer busted. You win!")
    #Bigger hand outcomes
    elif player_total > dealer_total:
        print("You have "+str(player_total)+" while the dealer has "+str(dealer_total)+". You win!")
    elif dealer_total > player_total:
        print("You have "+str(player_total)+" while the dealer has "+str(dealer_total)+". You lose!")

    response = input("Would you like to play again? Press any button to continue or 'n' to leave.")
    if response.lower() == 'n':
        playing = False

def make_bet():
    bet = 0
    response = input("You have $"+bankroll+", please place your bet or press 'n' to leave.")
    if response.lower() == 'n':
        playing = False
    while bet == 0:
        if response.lower() == 'n':
            playing = False
            return
        try:
            bet = int(response)
            playing = True
            return bet
        except ValueError:
            print("Please place a bet or press 'n' to leave.")

print("Welcome to Blackjack!")
while playing:
    bet = make_bet()
    if len(shoe) < 20:
        shuffle_up()
        
    deal_out()


print("Goodbye.")
shuffle_up()
deal_out()