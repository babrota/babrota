import string
import re
inc_str = r'''homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''


# get an additional sentence with last words of each existing sentence
def get_add_sent(input_str):
    sent_add = ''
    sent_new = []
    for word in input_str.lower().split():
        if '.' in word:
            sent_new.append(word[:-1])
    if sent_new:
        sent_new[0] = sent_new[0].capitalize()
        sent_add = ' '.join(sent_new) + '.'
    return sent_add


# get number of sentences in paragraph
def numb_sent(list_sent):
    num_sent = 0
    for n in range(len(list_sent)):
        if list_sent[n]:
            num_sent += 1
    return num_sent


# get nice sentence
def get_sent(one_sent):
    list_words = one_sent.lower().split()
    sentence = ' '.join(list_words)
    sentence = sentence[0].capitalize() + sentence[1:] + '. '
    return sentence


# get the index of the colon and the index of the letter that comes first after colon
def proc_colon(sent_colon):
    ind_colon = sent_colon.index(':')
    for ind_char, ch in enumerate(sent_colon):
        if ind_char > ind_colon:
            if ch.isalpha():
                return ind_colon, ind_char


# calculate number of whitespace in a text
def calc_wspc(txt):
    numb_whs = len(re.findall(r'\s', txt))
    return numb_whs


word_from = 'iz'
word_to = 'is'
spc = ' '
# convert all text to lowercase and some replaces
inc_str = inc_str.lower().replace(spc + word_from + spc, spc + word_to + spc).replace(' tex.', ' text.').replace('\n\n', '\n')

# add space before “ in Fix“iz”
list_quot_inside = re.findall(r'\S“.*?”', inc_str)
for repl_from in list_quot_inside:
    repl_from = str(repl_from)
    repl_to = repl_from[0] + spc + repl_from[1:]
    inc_str = inc_str.replace(repl_from, repl_to)

final_text = ''
list_nice_sent = []
# split  into paragraphs
par_list = inc_str.split('\n\n')
for p in range(len(par_list)):
    par = par_list[p]
    # split into sentences
    inc_str_list_sent = par.split('.')
    # count the number of sentences in a paragraph (split provides an additional sentence [])
    real_num_sent = numb_sent(inc_str_list_sent)
    for i in range(real_num_sent):
        # if inc_str_list_sent[i] is not empty
        if inc_str_list_sent[i]:
            # get nice sentence
            sent = get_sent(inc_str_list_sent[i])
            # processing when the sentence has :(colon)
            if ':' in sent:
                ind_col, ind_ch = proc_colon(sent)
                sent = sent[: ind_col+1] + '\n  ' + sent[ind_col+1: ind_ch] + sent[ind_ch].upper() + sent[ind_ch+1:]

            # add new sentence
            list_nice_sent.append(sent)

            # if this is the last sentence of the paragraph
            if real_num_sent - 1 == i:
                # if the second paragraph
                if p == 1:
                    # get new sentence
                    nice_sent_add = get_add_sent(inc_str)
                    # add new sentence to the end of second paragraph
                    list_nice_sent.append(nice_sent_add)
                # add \n after last sentence of every paragraph in any case
                list_nice_sent.append('\n   ')

# generate a final result concatenating a list of strings (nice sentences) using '' and remove spaces from the right
final_text = ''.join(list_nice_sent).rstrip()

if __name__ == '__main__':
    # display final text
    print(f'\nFinal result:\n\n{final_text}')
    # display number of whitespaces
    print(f'\nThe number of whitespace characters in this text is {calc_wspc(final_text)}.')
