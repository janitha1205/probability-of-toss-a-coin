# probability-of-toss-a-coin

flipping coin and see as probabilities of turn heads 
rand the function use to expect either one 
when rand give equal posibility of final selection as such head if value is less than 0.5 and tails when value is more than 0.5
there is a equalt chance of happing either one expectation.

# experimental probability

how likelly something to happen

number trails : n

heads occur: m

tails occur: n-m

P(head)= m/n

# experiment

toss the coin in n nuber of time and observed the heads occured in number out of trails 

# observed

P(trail) near to 0.5 as it has given same chance to ones occur 

# picking mables on box(3 red, 2 blue, 5 green)

P(red)= n(red)/n(all)=3/10

p(red')=1-p(red)=7/10

# servey results(probability using sets)


![image](https://github.com/user-attachments/assets/b22b178e-949a-48bf-a557-475e94fe3a4f)

## intersection of sets

this is where share common in paticular groups

ex:

N(like Cricket and Football)=2+5=7

P(like Cricket and Football)  =  N(like Cricket and Football)/N(all)  =  7/(21+25+30+3+5+2+10+4)  =  7/100 = 0.7 = 70%

## union of sets

all items include in both sets

N(like cricket or football) = 53

P(like cricket or football) = n(like cricket or football)/n(all)

= (n(cricket)+n(football)-n(like cricket and football))/n(all)

P(like cricket or football) = 53/100 = 0.53 = 53%

# conditional probability

def: the probability of an event occring give that another event has already occured

ex:

![image](https://github.com/user-attachments/assets/5a401cfd-4e31-4d4d-b822-88c8cd136267)



P(B|A)= N(B U A)/N(A)
= 5/26 = 0.192 = 19.2 %

ex:

![image](https://github.com/user-attachments/assets/b2dcb0a9-a171-4eac-a7f0-9e745bbe67ff)

probability of likes given by females

P(Likes| Female) = N(Likes U Female)/N(Female)

= 10/14 = 0.714 = 71.4%

# Multiplication Law

## independent events

that means events are not effected to each other


![image](https://github.com/user-attachments/assets/3ab41caf-0d3e-4c48-9033-43c4e47737c5)


P(A and B) or P(A,B)= P(A)*P(B)

ex:

when you fliping coin and roll a die, what is probability of heads and 3 occured at the same time

P(Heads)= 1/2

P(#3)= 1/6

P(Heads,#3) = P(Heads)*P(#3)
= 1/2 * 1/6
=1/12 = 0.08333 = 8.33 %

## dependent events

when there is a one event depend on other

P(A and B)=P(A)*P(B|A)

ex:

probability of two kings in row chosen out of rest of cards in a pack

P(king 1 and king 2) = P(king 1)*P(king 2 |king 1)

after one king taken out there is only 51 cards left out of 52 cards. in the mean time there is ony 3 king cards available

= (4/52)*(3/51) = 1/221 = 0.004523 = 0.4523 %

# permutation

know as how many arragement occured in set of elements out of total

ex:

this is known as when there is objecs A B C those are labled, out of it, how many arragement has to be done.

ABC
ACB
BAC
BCA
CAB
CBA

num of sets = 6 = 3*2*1 = 3!

Permutation is also known by this n! n element

elements: A B C

1 dig   2 dig    3 dig
 
P(3,2) x P(2,1) x P(1,1)

= 3  x  2   x 1

= 6

permutation written as P(n,r)

P(n,r) = n! / (n-r)!

ex: 10 runners are comit to maraton so how many arragement has in first 3 winners out of total

P(10,3) = 10!/7! = 8*9*10 = 720

ex:  there is a lock with 3 digit numbers to unlock so how possibile to opern at 1 run FYI: for any digit comprice of 60 combinations

P(correct) = 1/P(60,3) = 1 / (60*59*58) = 1 / 205320 = 4.871*e^-6 
= 0.0487 %

 # combinations

 in the situation where there is  unique feature in the set of object, number of items of unique features; however, there order arragement doesnt matters like purmutation,taken out in the stance known as combination

 notation

 C(n,r) = (n r) = n!/(n-r)!r!

 ex:

in group of 10 people how many of 3 people group could be created 

(10,3)  = C(10,3)  =  10! / (7! x 3!) = (10*9*8) / (3*2) =5*3*8 = 120

ex: kids 7 and adult 11, how posible the group having 6 people at a time there is only 1 kid in team 

P(1 kid) = n(ad=5,kid=1) / n(6 out of 18) = (7 1) * (11 5) / (18 6)

= (C(7,1) * C(11,5))/C(18,6) 

= 388080*6!*12!/120*18!

= 0.1742

= 17.42 %

# Probability distribution

## types

1 Normal

![image](https://github.com/user-attachments/assets/c090eb06-1029-4fa1-b98c-ee993558dd5d)

PDF:
 mean and standard deviation of data tells about propability of given varible value within the data for representaion model
 so in mean std are modelling parameeters of that can evaluate using experimental data

ex:
for the market value of product valivated in price of 125 Rs at deviation of 5.8 Rs what is probability of product valued in 155 Rs

mean = 125
std = 5.8
Z(val=155) = (x-mean)/std = (155-125) / 5.8 
= 5.172

pdf(z=155) = (1/(std*sqrt(2* pi))) *exp(-((z-mu)^2)/(2 x (std^2)))

using integrade pdf into pdf(0) to pdf(upper bound: end) as a fraction of from pdf(z=155) to pdf(upper bound: end) given the propability  

p(z>155) = 0.00000116 %

2 Exponential

![image](https://github.com/user-attachments/assets/c5b92fee-c38a-4284-8dd9-4f0584a16afd)


3 chi-squased

![image](https://github.com/user-attachments/assets/ea515b46-933b-4390-aa57-4d1e5fed1806)


4 uniform

![image](https://github.com/user-attachments/assets/f6002de3-0265-4f7a-9877-73aab64b60cb)

5 binomial distribution

probability of k sucess trails out of total n trails

p is the probability of sucess

P(X=k)=(n k)x p^k*(1-p)^(n-k)  {this is know as probabilty mass function}

ex: rolling die to expect #3 occured with 4 conecutive trails find probability for each occurance with considering binomial pdf

![image](https://github.com/user-attachments/assets/26a8fd93-b1b2-4360-ba9f-baecb13d09e8)

### expected value

E(#3) = n*p

p : probability of #3 occured
n : number of roll

E(#3)= 4*(1/6) 

4 trails exepectation is 0.67


### geometric probability distribution

this is where the none dependent distribution PMF(probability mass function)

p: probabilty of sucess

k: total number of sucess

P(X=k) = (1-p)^(k-1) * p

ex: rolls two dies to come up double probability of first sucess

p = 6/36

k=1

p(x=1) = (5/6)^0*(1/6)

= 1/6

= 0.1666

k=2

p(x=2) = (5/6)^1*(1/6)

= 5/36

= 0.14

k=3

p(x=3) = (5/6)^2*(1/6)

=  25/216

=0.1154

k=4

p(x=4) = (5/6)^3*(1/6)

=  0.0965

Q1:

probility of sucess at lesser than 3 rolls

 p(X<3) = p(X=1) + P(X=2) = 0.16 + 0.14 = 0.2

Q2:

probility of sucess at least 3 rolls

p(X<=3) = p(X=1) + P(X=2) + P(X=3) = 0.16 + 0.14 + 0.116 = 0.316
