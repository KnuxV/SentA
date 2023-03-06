"""
Created by kevin-desktop, on the 19/02/2023
READ sample Excel sheet and for each row (publication), ask the user to manually annotate the impact (=sentiment) of the
digital technology mentioned in the abstract
"""
import pandas as pd
import termcolor
import textwrap
import sys


def display_pub(row):
    row_to_print = row.iloc[0]
    abstract, title, keywords = row_to_print.AB, row_to_print.TI, row_to_print.DE

    if not isinstance(row_to_print.sdgkey, float):
        for key in row_to_print.sdgkey.split(", "):
            abstract = abstract.replace(key, termcolor.colored(key, 'green'))
            title = title.replace(key, termcolor.colored(key, 'green'))
            keywords = keywords.replace(key, termcolor.colored(key, 'green'))
    if not isinstance(row_to_print.dtkey, float):
        for key in row_to_print.dtkey.split(", "):
            abstract = abstract.replace(key, termcolor.colored(key, 'red'))
            title = title.replace(key, termcolor.colored(key, 'red'))
            keywords = keywords.replace(key, termcolor.colored(key, 'red'))

    print("Index: ", row.index.values[0])
    print(title)

    print("\nKeywords:")
    print(keywords, "\n")

    print(f"SDG: {row_to_print.SDG}")
    print(termcolor.colored(row_to_print.sdgkey, 'green'), "\n")
    lst_dt = ["AI", "robotics", "IOT", "big_data", "computing_infrastructure", "additive_manufacturing", "blockchain"]
    dt_in_pub = ""
    for dt in lst_dt:
        if row_to_print[dt]:
            dt_in_pub += str(dt) + " "
    print('Digital categories:', termcolor.colored(dt_in_pub, 'red'))
    print("Digital keywords in publications: ")
    print(termcolor.colored(row_to_print.dtkey, 'red'), "\n")

    print("Abstract: ")
    print(textwrap.fill(abstract, width=100,
                        break_long_words=False))
    print("\n")
    lst_term_cols = ['Term1', 'Term2', 'Term3', 'Term4', 'Term5']
    for term in lst_term_cols:
        if row_to_print[term] != "0":
            print(row_to_print[term].replace("\n", ", "))
    res = input("Annotation? Pos/Neu/Neg\n")
    score = input("Score: \n")
    comments = input("Comments: \n")
    return [res, score, comments]


def annotate_row(excel_path, comments_path, user):
    df = pd.read_excel(excel_path, sheet_name="Sheet1", index_col=0)
    df_comments = pd.read_excel(comments_path)
    cond_user = df['Annotator'] == user
    df_sample = df[cond_user]

    # Only keep pubs not annotated yet
    cond_na = df_sample['Annotation'].isna()
    df_sample = df_sample[cond_na]
    nb_row_to_annotate = len(df_sample)

    print(f"You have already annotated {35 - len(df_sample)} out of 35, {nb_row_to_annotate} left.\n")

    if nb_row_to_annotate == 0:
        print("Finished")
        return False
    row = df_sample.sample(1)
    res, score, comments = display_pub(row)
    df.loc[row.index, "Annotation"] = res
    df.to_excel(excel_path)

    row = [row.index.values[0], res, score, comments]
    print(row)
    print(df_comments.columns)
    new_df = pd.DataFrame([row], columns=df_comments.columns)
    df_comments = pd.concat([df_comments, new_df], axis=0, ignore_index=True)

    df_comments.to_excel(comments_path, engine='openpyxl', index=False)
    return True


def main(sample_path, comment_path, user):
    cont = True
    while cont:
        ans = input("Annotate a new publication? (y/n)\n")
        if ans in ['Yes', 'yes', 'y', 'Y']:
            cont = annotate_row(excel_path=sample_path, comments_path=comment_path, user=user)
        else:
            print('Exiting the script.')
            break


if __name__ == '__main__':
    try:
        excel_path = sys.argv[1]
        comment_path = sys.argv[2]
        user = sys.argv[3]
        main(excel_path, comment_path, user)
    except IndexError:
        print("Use: python manual_annotation_sentiment.py path_sample path_comment first_name")
        print("For example:")
        print("python manual_annotation_sentiment.py sample_SB.xlsx comments_SB.xlsx Claudia")
