#!/user/bin/bash
WEBSITE_DIR='/Users/Zaaron/Code/bzreinhardt.github.io'
python $WEBSITE_DIR/_scripts/compile_medb_to_website.py
python $WEBSITE_DIR/_scripts/generate_questions.py
python $WEBSITE_DIR/_scripts/tag_generator.py
