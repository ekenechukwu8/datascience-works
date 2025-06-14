def time_to_buy_tickets(tickets, k):
    time = 0
    for i in range(len(tickets)):
        if i <= k:
            time += min(tickets[i], tickets[k])
        else:
            time += min(tickets[i], tickets[k] - 1)
    return time

# Example usage
if __name__ == "__main__":
    tickets = [2, 3, 2]
    k = 2
    print("Time to buy tickets:", time_to_buy_tickets(tickets, k))
