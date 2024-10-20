
def user_name():
    username = input("Enter Your Name::: ")
    return username

def main_operation(arr, answers):
    for i in range(len(arr)):
      while True:
            print(arr[i])
            input_ = input("Enter your choice (A/B): ").upper()
            if input_ == "A" or input_ == "B":
                answers[i] = input_
                break
            else:
                print("Invalid choice. Please enter A or B.")


def personas_sum(arr, answers, chosen):
    extrovert = 0
    introvert = 0
    for i in range(0, len(arr), 4):
        if answers[i] == "A":
            extrovert += 1
            print(arr[i][0])
        if answers[i] == "B":
            introvert += 1
            print(arr[i][1])
        if extrovert > introvert:
            chosen[0] = "E"
        if introvert > extrovert:
            chosen[0] = "I"
    print("Extrovert : ", extrovert)
    print("Introvert : ", introvert)

def personas_sum_two(arr, answers, chosen):
    sensitive = 0
    intuitive = 0
    for i in range(1, len(arr), 4):
        if answers[i] == "A":
            sensitive += 1
            print(arr[i][0])
        if answers[i] == "B":
            intuitive += 1
            print(arr[i][1])
        if sensitive > intuitive:
            chosen[1] = "S"
        if intuitive > sensitive:
            chosen[1] = "N"
    print("Sensitive : ", sensitive)
    print("Intuitive : ", intuitive)

def personas_sum_three(arr, answers, chosen):
    thinking = 0
    feeling = 0
    for i in range(2, len(arr), 4):
        if answers[i] == "A":
            thinking += 1
            print(arr[i][0])
        if answers[i] == "B":
            feeling += 1
            print(arr[i][1])
        if thinking > feeling:
            chosen[2] = "T"
        if feeling > thinking:
            chosen[2] = "F"
    print("Thinking : ", thinking)
    print("Feeling : ", feeling)

def personas_sum_four(arr, answers, chosen):
    judging = 0
    perceptive = 0
    for i in range(3, len(arr), 4):
        if answers[i] == "A":
            judging += 1
            print(arr[i][0])
        if answers[i] == "B":
            perceptive += 1
            print(arr[i][1])
        if judging > perceptive:
            chosen[3] = "J"
        if perceptive > judging:
            chosen[3] = "P"
    print("Judging : ", judging)
    print("Perceptive : ", perceptive)

def print_personality_type(answers, chosen):
    if chosen[0] == "E" and chosen[1] == "S" and chosen[2] == "F" and chosen[3] == "P":
        print("ESFP (Entertainer) is a personality type with the Extraverted, Observant, Feeling, and Prospecting traits. These people love vibrant experiences, engaging in life eagerly and taking pleasure in discovering the unknown. They can be very social, often encouraging others into shared activities.")
    elif chosen[0] == "E" and chosen[1] == "S" and chosen[2] == "T" and chosen[3] == "P":
        print("ESTP (Entrepreneur) is a personality type with the Extraverted, Observant, Thinking, and Prospecting traits. They tend to be energetic and action-oriented, deftly navigating whatever is in front of them. They love uncovering life’s opportunities, whether socializing with others or in more personal pursuits.")
    elif chosen[0] == "I" and chosen[1] == "S" and chosen[2] == "F" and chosen[3] == "P":
        print("ISFP (Adventurer) is a personality type with the Introverted, Observant, Feeling, and Prospecting traits. They tend to have open minds, approaching life, new experiences, and people with grounded warmth. Their ability to stay in the moment helps them uncover exciting potentials.")
    elif chosen[0] == "I" and chosen[1] == "S" and chosen[2] == "T" and chosen[3] == "P":
        print("ISTP (Virtuoso) is a personality type with the Introverted, Observant, Thinking, and Prospecting traits. They tend to have an individualistic mindset, pursuing goals without needing much external connection. They engage in life with inquisitiveness and personal skill, varying their approach as needed.")
    elif chosen[0] == "E" and chosen[1] == "S" and chosen[2] == "F" and chosen[3] == "J":
        print("ESFJ (Consul) is a personality type with the Extraverted, Observant, Feeling, and Judging traits. They are attentive and people-focused, and they enjoy taking part in their social community. Their achievements are guided by decisive values, and they willingly offer guidance to others.")
    elif chosen[0] == "E" and chosen[1] == "S" and chosen[2] == "T" and chosen[3] == "J":
        print("ESTJ (Executive) is a personality type with the Extraverted, Observant, Thinking, and Judging traits. They possess great fortitude, emphatically following their own sensible judgment. They often serve as a stabilizing force among others, able to offer solid direction amid adversity.")
    elif chosen[0] == "I" and chosen[1] == "S" and chosen[2] == "F" and chosen[3] == "J":
        print("ISFJ (Defender) is a personality type with the Introverted, Observant, Feeling, and Judging traits. These people tend to be warm and unassuming in their own steady way. They’re efficient and responsible, giving careful attention to practical details in their daily lives.")
    elif chosen[0] == "I" and chosen[1] == "S" and chosen[2] == "T" and chosen[3] == "J":
        print("ISTJ (Logistician) is a personality type with the Introverted, Observant, Thinking, and Judging traits. These people tend to be reserved yet willful, with a rational outlook on life. They compose their actions carefully and carry them out with methodical purpose.")
    elif chosen[0] == "E" and chosen[1] == "N" and chosen[2] == "F" and chosen[3] == "P":
        print("ENFP (Campaigner) is a personality type with the Extraverted, Intuitive, Feeling, and Prospecting traits. These people tend to embrace big ideas and actions that reflect their sense of hope and goodwill toward others. Their vibrant energy can flow in many directions.")
    elif chosen[0] == "E" and chosen[1] == "N" and chosen[2] == "F" and chosen[3] == "J":
        print("ENFJ (Protagonist) is a personality type with the Extraverted, Intuitive, Feeling, and Judging traits. These warm, forthright types love helping others, and they tend to have strong ideas and values. They back their perspective with the creative energy to achieve their goals.")
    elif chosen[0] == "I" and chosen[1] == "N" and chosen[2] == "F" and chosen[3] == "P":
        print("INFP (Mediator) is a personality type with the Introverted, Intuitive, Feeling, and Prospecting traits. These rare personality types tend to be quiet, open-minded, and imaginative, and they apply a caring and creative approach to everything they do.")
    elif chosen[0] == "I" and chosen[1] == "N" and chosen[2] == "F" and chosen[3] == "J":
        print("INFJ (Advocate) is a personality type with the Introverted, Intuitive, Feeling, and Judging traits. They tend to approach life with deep thoughtfulness and imagination. Their inner vision, personal values, and a quiet, principled version of humanism guide them in all things.")
    elif chosen[0] == "E" and chosen[1] == "N" and chosen[2] == "T" and chosen[3] == "P":
        print("ENTP (Debater) is a personality type with the Extraverted, Intuitive, Thinking, and Prospecting traits. They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility. They pursue their goals vigorously despite any resistance they might encounter.")
    elif chosen[0] == "E" and chosen[1] == "N" and chosen[2] == "T" and chosen[3] == "J":
        print("ENTJ (Commander) is a personality type with the Extraverted, Intuitive, Thinking, and Judging traits. They are decisive people who love momentum and accomplishment. They gather information to construct their creative visions but rarely hesitate for long before acting on them.")
    elif chosen[0] == "I" and chosen[1] == "N" and chosen[2] == "T" and chosen[3] == "P":
        print("INTP (Logician) is a personality type with the Introverted, Intuitive, Thinking, and Prospecting traits. These flexible thinkers enjoy taking an unconventional approach to many aspects of life. They often seek out unlikely paths, mixing willingness to experiment with personal creativity.")
    elif chosen[0] == "I" and chosen[1] == "N" and chosen[2] == "T" and chosen[3] == "J":
        print("INTJ (Architect) is a personality type with the Introverted, Intuitive, Thinking, and Judging traits. These thoughtful tacticians love perfecting the details of life, applying creativity and rationality to everything they do. Their inner world is often a private, complex one.")



def main():
    arr = [
        ["(A:) Expend energy, enjoy groups", "\t", " (B:) Conserve energy, enjoy one-on-one"],
        ["(A:) Interpret literally", "\t", "(B:) look for meaning and possibilities"],
        ["(A:) logical, thinking, question", "\t", "(B:) empathetic, feeling, accomodating"],
        ["(A:) Organized,Orderly", "\t", "(B:) Flexible, adaptable"],
        ["(A:) More outgoing, think out loud", "\t", "(B:) more reserved, think to yourself"],
        ["(A:) Practical, realistic, experiential", "\t", "(B:) imaginative, innovative, theoretical"],
        ["(A:) Candid, straight-foward, frank", "\t", "(B:) tactful, kind, encouraging"],
        ["(A:) Plan, schedule", "\t", "(B:) unplanned, spontaneous"],
        ["(A:) Seek many tasks, public activities, interaction with others", "\t", "(B:) seek private, solitary activities with quiet to concentrate"],
        ["(A:) Standard, usual, conventional", "\t", "(B:) different, novel, unique"],
        ["(A:) Firm, tend to criticize, hold the line", "\t", "(B:) gentle, tend to appreciate, conciliation"],
        ["(A:) Regulated, structured", "\t", "(B:) easy-going, live and let live"],
        ["(A:) External, communicate, express yourself", "\t", "(B:) internal, reticent, keep to yourself"],
        ["(A:) Focus on here-and-now", "\t", "(B:) look to the future, global perspective, big picture"],
        ["(A:) Tough-mided, just", "\t", "(B:) tender-hearted, merciful"],
        ["(A:) Preparation, plan ahead", "\t", "(B:) go with the flow, adapt as you go"],
        ["(A:) Active, initiative", "\t", "(B:) reflective, deliberate"],
        ["(A:) Facts, Things, What is", "\t", "(B:) ideas, dreams, what could be, philosophical"],
        ["(A:) Matterof facts, issue-oriented", "\t", "(B:) sensitive, people-oriented, compassionate"],
        ["(A:) Control, govern", "\t", "(B:) latitude, freedom"]
    ]
    answers = [""] * 20
    chosen = [""] * 4

    print("Choose Either A or B ")
    user_name()
    main_operation(arr, answers)
    personas_sum(arr, answers, chosen)
    personas_sum_two(arr, answers, chosen)
    personas_sum_three(arr, answers, chosen)
    personas_sum_four(arr, answers, chosen)
    print("Personality Type: " + chosen[0] + chosen[1] + chosen[2] + chosen[3])
    print_personality_type(answers, chosen)

if __name__ == "__main__":
    main()
