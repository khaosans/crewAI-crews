from textwrap import dedent

class TaskPrompts():
    def expand(self):
        return dedent("""
            THIS IS A GREAT IDEA! Analyze and expand it 
            by conducting comprehensive research on task management.

            
            Final answer MUST be a comprehensive task board research  
            detailing why this task board is beneficial, the value 
            proposition, unique features, and how it addresses user pain points.

            IDEA: 
            ----------
            {idea}
        """)

    def create_user_stories(self):
        return dedent("""
            Verify the user stories created based on the research and chosen template. 
            Break down each user story into actionable tasks for the front-end, 
            back-end, and QA teams. Ensure that each task is clear, concise, and 
            includes acceptance criteria.

            Your final answer MUST be a detailed breakdown of user stories 
            into tasks, specifying which team is responsible for each task.
        """)

    def choose_templates(self):
        return dedent("""
            Based on the research and the chosen template, 
            create user stories that capture the needs and 
            expectations of users interacting with the task board. 
            Each user story should follow the format: "As a [user type], 
            I want [goal] so that [reason]."

            Your final answer MUST be a list of user stories 
            that are clear, concise, and actionable.
        """)

    def refine_templates(self):
        return dedent("""
            Review the available templates for task boards and choose the one 
            that best suits the idea below. You MUST copy the 
            chosen template to the project folder and then read 
            the src/components in the directory you just copied 
            to decide which component files should be updated 
            to create the task board for the idea below.

            - YOU MUST READ THE DIRECTORY BEFORE CHOOSING THE FILES.      
            - YOU MUST NOT UPDATE any Pricing components.
            - YOU MUST UPDATE ONLY the 4 most important components.

            Your final answer MUST be ONLY a JSON array of 
            components' full file paths that need to be updated.

            IDEA 
            ----------
            {idea}
        """)

    def update_board(self):
        return dedent("""
            READ the ./[chosen_template]/src/app/board.jsx OR
            ./[chosen_template]/src/app/(main)/board.jsx (main with the parenthesis) 
            to learn its content and then write an updated 
            version to the filesystem that removes any 
            section-related components that are not in our 
            list from the returns. Keep the imports.

            Final answer MUST BE ONLY a valid JSON list with 
            the full path of each of the components we will be 
            using, the same way you got them.

            RULES
            -----
            - NEVER ADD A FINAL DOT to the file content.
            - NEVER WRITE \\n (newlines as string) on the file, just the code.
            - NEVER FORGET TO CLOSE THE FINAL BRACKET (}})
            - NEVER USE COMPONENTS THAT ARE NOT IMPORTED.
            - ALL COMPONENTS USED SHOULD BE IMPORTED, don't make up components.
            - Save the file with a `.jsx` extension.
            - Return the same valid JSON list of the components you got.

            You'll get a $100 tip if you follow all the rules!

            Also, update any necessary text to reflect this task board
            is about the idea below.

            IDEA 
            ----------
            {idea}
        """)

    def component_content(self):
        return dedent("""
            A developer will update the src/components (code below),
            return a list of good options of texts to replace 
            EACH INDIVIDUAL existing text on the component, 
            the suggestion MUST be based on the task board idea below, 
            and also MUST be similar in length to the original 
            text; we need to replace ALL TEXT.

            NEVER USE Apostrophes for contraction! You'll get a $100 
            tip if you do your best work!
        """)

        {idea}
    def update_component(self, ):
        return dedent(f"""
            YOU MUST USE the tool to write an updated 
            version of the React component to the file 
            system in the following path: 
            replacing the text content with the suggestions 
            provided.

            You only modify the text content; you don't add 
            or remove any components.

            You first write the file, then your final answer 
            MUST be the updated component content.

            RULES
            -----
            - Remove all the links; this should be a single-page task board.
            - Don't make up images, videos, gifs, icons, logos, etc.
            - Keep the same style and Tailwind classes.
            - MUST HAVE `'use client'` at the beginning of the code.
            - href in buttons, links, NavLinks, and navigations should be `#`.
            - NEVER WRITE \\n (newlines as string) on the file, just the code.
            - NEVER FORGET TO CLOSE THE FINAL BRACKET (}}) in the file.
            - Keep the same component imports and don't use new components.
            - NEVER USE COMPONENTS THAT ARE NOT IMPORTED.
            - ALL COMPONENTS USED SHOULD BE IMPORTED, don't make up components.
            - Save the file with a `.jsx` extension.

            If you follow the rules, I'll give you a $100 tip!!! 
            MY LIFE DEPENDS ON YOU FOLLOWING IT!

        """)

    def qa_component(self):
        return dedent(f"""
            Check the React component code to make sure 
            it's valid and abides by the rules below. 
            If it doesn't, then write the correct version to 
            the file system using the write file tool into 
            the following path: src/components.

            Your final answer should be a confirmation that 
            the component is valid and abides by the rules, and if
            you had to write an updated version to the file system.

            RULES
            -----
            - NEVER USE Apostrophes for contraction!
            - ALL COMPONENTS USED SHOULD BE IMPORTED.
            - MUST HAVE `'use client'` at the beginning of the code.
            - href in buttons, links, NavLinks, and navigations should be `#`.
            - NEVER WRITE \\n (newlines as string) on the file, just the code.
            - NEVER FORGET TO CLOSE THE FINAL BRACKET (}})
            - NEVER USE COMPONENTS THAT ARE NOT IMPORTED.
            - ALL COMPONENTS USED SHOULD BE IMPORTED, don't make up components.
            - Always use `export function` for the component class.

            You'll get a $100 tip if you follow all the rules!
        """)
