letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>
            '''
print(letter.replace("<|Name|>", "Agent").replace("<|Date|>", "2/10/2026"))