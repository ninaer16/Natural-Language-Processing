# example that uses the nltk_contrib FST class
from nltk.nltk_contrib.fst.fst import *

class myFST(FST):    
    def recognize(self, iput, oput):

        # insert your codes here
        #self.inp = iput.split()
        #self.outp = oput.split()
        self.inp = list(iput)
        self.outp = list(oput)
        #f.transduce("abc")        
        
        # Check if the output matches the transduction of the input
        return list(oput) == self.transduce(list(iput))

f = myFST('example')

# first add the states in the FST
for i in range(1,38):
    f.add_state(str(i)) # add states '1' .. '38'

# add one initial state
f.initial_state = '1' # -> 1

# add all transitions
#fit-nèet
f.add_arc('1', '2', ['fit'], ['fit']) # 1 -> 2 [fit:fit]
f.add_arc('2', '3', ['-nèet'], ['-ness']) # 2 -> 3 [-nèet:-ness]

#mai-khroo-foon
f.add_arc('1', '4', ['mai'], ['mi']) # 0 -> 3 [-mai:-mi]
f.add_arc('4', '5', ['-khroo'], ['-cro']) # 3 -> 4 [-khroo:-cro]
f.add_arc('5', '6', ['-foon'], ['-phone']) # 4 -> 5 [-foon:-phone]

#mai-kroh-wáyp
f.add_arc('4', '7', ['-kroh'], ['-cro']) # 3 -> 6 [-kroh:-cro]
f.add_arc('7', '8', ['-wáyp'], ['-wave']) # 6 -> 7 [-wáyp:-wave]

#bay-bêe
f.add_arc('1', '9', ['bay'], ['ba']) # 1 -> 10 [bay:ba]
f.add_arc('9', '10', ['-bêe'], ['-by']) # 10 -> 11 [-bêe:-by]

#bay-ger-rêe
f.add_arc('9', '11', ['-ger'], ['-ke']) # 10 -> 11 [-ger:-ke]
f.add_arc('11', '12', ['-rêe'], ['-ry']) # 12 -> 11 [-rêe:-by]

#kaa-fây
f.add_arc('1', '13', ['kaa'], ['ca']) # 1 -> 14 [kaa:ca]
f.add_arc('13', '14', ['-fây'], ['-fé']) # 14 -> 15 [-fây:-fé]

#kaa-fay-een
f.add_arc('13', '15', ['-fay'], [' ']) # 14 -> 16 [-fay: ]
f.add_arc('15', '16', ['-een'], ['-ffeine']) # 16 -> 17 [-een:-ffeine]

#bluu-booe-rîi
f.add_arc('1', '17', ['bluu'], ['blue']) # 1 -> 18 [bluu:blue]
f.add_arc('17', '18', ['-booe'], ['-ber']) # 18 -> 19 [-booe:-ber]
f.add_arc('18', '19', ['-rîi'], ['-ry']) # 19 -> 20 [-rîi:-ry]

#sà-dtraaw-booe-rîi
f.add_arc('1', '20', ['sà'], ['st']) # 1 -> 21 [-een:-ffeine]
f.add_arc('20', '17', ['-dtraaw'], ['-raw']) # 21 -> 22 [-dtraaw:-raw]

#ree-môht
f.add_arc('1', '21', ['ree'], [' ']) # 1 -> 22 [ree: ]
f.add_arc('21', '22', ['-môht'], ['remote']) # 22 -> 23 [-môht:remote]

#ree-son
f.add_arc('21', '23', ['-son'], ['reason']) # 22 -> 23 [-son:reason]

#wee-dee-oh
f.add_arc('1', '24', ['wee'], ['vi']) # 1 -> 25 [wee:vi]
f.add_arc('24', '25', ['-dee'], ['']) # 25 -> 26 [-dee: ]
f.add_arc('25', '26', ['-oh'], ['-deo']) # 26 -> 27 [-oh:-deo]

#wee-sâa
f.add_arc('24', '27', ['-sâa'], ['-sa']) # 25 -> 28 [-sâa:-sa]

#loh-chân
f.add_arc('1', '28', ['loh'], ['lo']) # 1 -> 29 [loh:lo]
f.add_arc('28', '29', ['-chân'], ['-tion']) # 29 -> 30 [-chân:-tion]

#bproh-jèk
f.add_arc('1', '30', ['bproh'], ['pro']) # 1 -> 31 [bproh:pro]
f.add_arc('30', '31', ['-jèk'], ['-ject']) # 31 -> 32 [-jèk:-ject]

#bproh-moh-chân
f.add_arc('30', '28', ['-moh'], ['-mo']) # 31 -> 30 [-moh:-mo]

#kaa-bpoo-chí-noh
f.add_arc('13', '32', ['-bpoo'], ['-ppu']) # 14 -> 33 [-bpoo:-ppu]
f.add_arc('32', '33', ['-chí'], ['-ci']) # 33 -> 34 [-chí:-ci]
f.add_arc('33', '34', ['-noh'], ['-no']) # 34 -> 35 [-noh:-no]

#kaa-boh-hai-dràyt
f.add_arc('13', '35', ['-boh'], ['-bo']) # 14 -> 36 [-boh:-bo]
f.add_arc('35', '36', ['-hai'], ['-hy']) # 37 -> 38 [-hai:-hy]
f.add_arc('36', '37', ['-dràyt'], ['-drate']) # 38 -> 39 [-dràyt:-drate]

# add final/accepting state(s)
f.set_final('3') # for paths ending with '-nèet'
f.set_final('6') # for paths ending with '-foon'
f.set_final('8') # for paths ending with '-wáyp'
f.set_final('10') # for paths ending with '-bêe'
f.set_final('12') # for paths ending with '-rêe'
f.set_final('14') # for paths ending with '-fây'
f.set_final('16') # for paths ending with '-een'
f.set_final('19') # for paths ending with '-rîi'
f.set_final('22') # for paths ending with '-môht'
f.set_final('23') # for paths ending with '-son'
f.set_final('26') # for paths ending with '-oh'
f.set_final('27') # for paths ending with '-sâa'
f.set_final('29') # for paths ending with '-chân'
f.set_final('31') # for paths ending with '-jèk'
f.set_final('34') # for paths ending with '-noh'
f.set_final('37') # for paths ending with '-dràyt'

# use the nltk transduce function
#print(" ".join(f.transduce("a b a b b".split())))

# use the recognize function defined in myFST
#if f.recognize("a b a b b", "1 1 - 1 1"):
# Define test cases
test_cases = [
    (['fit', '-nèet'], ['fit', '-ness']),
    (['mai', '-khroo', '-foon'], ['mi', '-cro', '-phone']),
    (['mai', '-kroh', '-wáyp'], ['mi', '-cro', '-wave']),
    (['bay', '-bêe'], ['ba', '-by']),
    (['bay', '-ger', '-rêe'], ['ba', '-ke', '-ry']),
    (['kaa', '-fây'], ['ca', '-fé']),
    (['kaa', '-fay', '-een'], ['ca', '-ffeine']),
    (['bluu', '-booe', '-rîi'], ['blue', '-ber', '-ry']),
    (['sà', '-dtraaw', '-booe', '-rîi'], ['st', '-raw', '-ber', '-ry']),
    (['ree', '-son'], ['reason']),
    (['wee', '-dee', '-oh'], ['vi', '-deo']),
    (['wee', '-sâa'], ['vi', '-sa']),
    (['loh', '-chân'], ['lo', '-tion']),
    (['bproh', '-jèk'], ['pro', '-ject']),
    (['bproh', '-moh', '-chân'], ['pro', '-mo', '-tion']),
    (['kaa', '-bpoo', '-chí', '-noh'], ['ca', '-ppu', '-ci', '-no']),
    (['kaa', '-boh', '-hai', '-dràyt'], ['car', '-bo', '-hy', 'drate']),
]

# Check each test case and write results to a file
with open("Thaiglish-trans.dat", "w") as file:
    for inp, outp in test_cases:
        # Join the words in the input and output lists and format them
        input_str = ' '.join(inp)
        output_str = ' '.join(outp)
        
        # Write the input-output mapping in the desired format
        file.write(f"{input_str} --> {output_str}\n")
print("Transliteration mappings saved to 'Thaiglish-trans.dat'")

try:
    disp = FSTDisplay(f)
except Exception as e:
    print("FSTDisplay not available:", e)
