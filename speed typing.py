


# def typing(script):
#     words = script.split()
#     input_text = input("enter you scripts: ")
#     list = []
#     for word in words:
#         list.append(word)
#         if input_text == script[len(word)]:
#             print('100%')
#         else:
#             print('fail')    
#     return (f'this scripts = {len(list)} words.')
# print(typing('returns the number of times the specified element appears in the list. Example. # create a list numbers'))    


import time

def calculate_typing_speed(script, time_taken):
    words = script.split()
    num_words = len(words)
    words_per_minute = (num_words / time_taken) * 60
    return words_per_minute

def typing_test(script, time_limit):
    print("Type the following script:")
    print(script)
    input("Press Enter when you are ready to start the typing test.")
    
    print(f"\nThe timer is set for {time_limit} seconds.")
    time.sleep(time_limit)
    
    start_time = time.time()
    input_text = input("Start typing: ")
    end_time = time.time()
    time_taken = end_time - start_time
    
    user_words = input_text.split()
    accuracy = sum(1 for a, b in zip(user_words, script.split()) if a == b) / len(script.split()) * 100
    
    typing_speed = calculate_typing_speed(script, time_taken)
    
    print("\nTyping Test Results:")
    print(f"Your typing speed: {typing_speed:.2f} words per minute.")
    print(f"Accuracy: {accuracy:.2f}%")

script_to_type = 'Returns the number of times the specified element appears in the list. Example. # create a list numbers'
time_limit_in_seconds = 10
typing_test(script_to_type, time_limit_in_seconds)

