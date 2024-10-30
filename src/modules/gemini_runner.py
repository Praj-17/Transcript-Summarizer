import google.generativeai as genai
from SimplerLLM.language.llm import LLM, LLMProvider
from SimplerLLM.language.llm_addons import generate_pydantic_json_model as gen_json
from dotenv import load_dotenv
# from src.constants import SummaryModel
import os
load_dotenv()
import re
import json
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
from src.constants import SummaryModel









class GeminiRunner:
    def __init__(self) -> None:
        self.llm_instance = LLM.create(provider=LLMProvider.GEMINI, model_name=os.getenv("GEMINI_MODEL_NAME"))
        with open(os.getenv("summary_prompt_file_location"), "r") as f:
            self.prompt = f.read()
    def _format_prompt(self, company_name, context):
        return self.prompt.format(company_name = company_name, context = context)

    def generate_summary_response(self, context, company_name):
        prompt = self._format_prompt(context=context, company_name= company_name)
        json_response = gen_json(model_class=SummaryModel,prompt=prompt, llm_instance=self.llm_instance)
        # Find all matches and convert to a dictionary
        return json_response.to_json_schema()

if __name__ == "__main__":

    context = """






Corporate Office - One Skymark, Tower-D, Plot No. H-10B, Sector-98, Noida-201304
T: +91120 4770770   F: +91120 4770771 CIN: L72200DL2000PLC108985
Registered Office - 136, First Floor, Devika Tower, Nehru Place, New Delhi-110019
One 97 Communications Limited
compliance.officer@paytm.com
www.paytm.com

October 29, 2024

BSE Limited
Department of Corporate Services
Phiroze Jeejeebhoy Towers,
Dalal Street, Fort,
Mumbai - 400 001

Scrip Code: 543396
National Stock Exchange of India Limited
The Listing Department
Exchange Plaza,
Bandra Kurla Complex,
Mumbai - 400 051

Symbol: PAYTM


Sub.:  Disclosure under Regulation 30 of the SEBI (Listing Obligations and Disclosure Requirements)
Regulations, 2015 - Transcript of the earnings conference call conducted on October 22, 2024



Dear Sir / Ma’am,

Pursuant to Regulation 30 of the SEBI (Listing Obligations and Disclosure Requirements) Regulations,
2015, please find enclosed the transcript of the earnings conference call, conducted on October 22,
2024, on financial results of the Company for the quarter and half year ended September 30, 2024.

The transcript is also available on the website of the Company at https://ir.paytm.com/financial-
results.

Kindly take the same on record.

Thanking you

Yours Sincerely,
For One 97 Communications Limited


Sunil Kumar Bansal
Company Secretary and Compliance Officer

Encl. as Above

SUNIL KUMAR
BANSAL
Digitally signed by SUNIL
KUMAR BANSAL
Date: 2024.10.29 15:44:26
+05'30'
Paytm | Q2FY25 Earnings Call |
Call Date : October 22, 2024 | Time: 17:00 PM Indian Standard Time
__________________________________________________________________________________________________________
Disclaimer:
By reading this call transcript you agree to be bound as follows: This earnings call with the management of
One 97 Communications Limited (“Company”) is for information purposes only without regards to specific
objectives, financial situations or needs of any particular person and is not and nothing in it shall be construed
as an invitation, offer, solicitation, recommendation or advertisement in respect of the purchase or sale of any
securities of the Company or any affiliates in any jurisdiction or as an inducement to enter into investment
activity and no part of it shall form the basis of or be relied upon in connection with any contract or
commitment or investment decision whatsoever. This earnings call does not take into account, nor does it
provide any tax, legal or investment advice or opinion regarding the specific investment objectives or financial
situation of any person. The information to be presented and discussed on this earnings call is confidential and
proprietary to the Company and/or its affiliates and no part of it or its subject matter be used, recorded,
reproduced, copied, distributed, shared, or disseminated, directly or indirectly, to any other person or
published in whole or in part for any purpose, in any manner whatsoever.
Statements or comments made on this earnings call may include certain statements that are, or may be
deemed to be, “forward-looking statements” and relate to the Company and its financial position, business
strategy, events and courses of action. Forward-looking statements and financial projections are based on the
opinions and estimates of management at the date the statements are made and are subject to a variety of
risks and uncertainties and other factors that could cause actual events or results to differ materially from
those anticipated in the forward-looking statements and financial projections. 
We, or any of our affiliates, shareholders, directors, employees, or advisors, as such, make no representations
or warranties, express or implied, as to, and do not accept any responsibility or liability with respect to, the
fairness, accuracy, completeness or correctness of any information or opinions contained herein and accept no
liability whatsoever for any loss, howsoever, arising from any use or reliance on the information presented and
discussed in this earnings call. The information contained herein is subject to change without any obligation to
notify any person of such revisions or change and past performance is not indicative of future results. 
It is clarified that this earnings call, and the information discussed and presented herein, is not intended to be
an offer for subscription or sale of any securities or inviting offers or invitations to offer or solicitation to offer
from the public (including any section thereof) or any class of investors. No rights or obligations of any nature
are created or shall be deemed to be created by the information presented and discussed on this earnings call.
This document has not been and will not be reviewed or approved by a regulatory authority in India or by any
stock exchange in India. No rights or obligations of any nature are created or shall be deemed to be created by
the contents of this document.
________________________________________________________________________________________________________________________
Moderator: Thank you for joining and welcome to Paytm's earnings call to discuss our financial results
for the quarter ending on September 30th, 2024. We will start our call with Q&A after introduction to
the management. From Paytm's management, we have with us Mr. Vijay Shekhar Sharma, Founder and
CEO, Mr. Madhur Deora, President and Group CFO and Mr. Anuj Mittal, SVP, Investor Relations. A few
standard announcements before we begin. The information to be presented and discussed here should
not be recorded, reproduced or distributed in any manner. Some statements made today may be
forward looking in nature. Actual events may differ materially from those anticipated in such forward
looking statements. Finally, this earnings call is scheduled for 60 minutes. A replay of this earnings call
and transcript will be made available on the company's website subsequently. We will start our Q&A
now. If you seek to ask a question, kindly utilize the raise hand feature on your zoom dashboard. Please
ensure that your name is visible as your name, last name followed by your company name for us to be
able to identify you. We will unmute your line and take questions in the respective sequence of the
raised hands. Our first question is from Alok Srivastava from UBS. Alok, you may please go ahead.
Alok Srivastava: Yeah. Hi, everyone. I think the first question is if Madhur or Vijay, if you could explain
this DLG model with an example in terms of how revenue will accrue, how cost will be there, I think it
will be helpful for everyone.
Mr. Madhur Deora, President and Group CFO: Yeah. Hi. Thank you Alok, I can begin to answer that. So,
as you know, in our previous model, without DLG, which is a model that we continue with certain
partners, we have a sourcing fee, which we have described earlier as 3.5 - 4%. So that continues as is. We
give a DLG to our partners upfront, which obviously is well within the regulatory guidelines. So we give
that DLG we have, as mentioned in the earnings release, we expensed that entirely currently in the
quarter in which it was given. So in the last quarter we have expensed all the DLG that we have given and
as a result of this, we get higher collection revenue during the life of the loan. The overall take rate, net
of DLG, still works out and here we're talking about merchant loans because we have given data only for
merchant loans. The overall take rate during the life of the loan, net of DLG cost, still works out to be
north of 5%, which was, which is, and as you know earlier we did not have a concept of net of DLG cost.
So we had an overall take rate. We think that the overall take rate will still be north of 5%, net of DLG
cost. So we do expect a significant amount of collection revenue over the life of the loan under the DLG
model.
Mr. Vijay Shekhar Sharma, Founder and CEO: This is Vijay. Thank you for joining. Also, I would go ahead
and say that we were reviewing our all regulated businesses and we were seeing what is the market
practice and regulatory, sort of guidance on those businesses. And as you are aware, the more or less
industry had matured or materialized and had reached towards a DLG based structure. While our
commercial model never had any challenge from any audits, etc. but our lenders did look at it. But we
were more about that how can we make the business very much aligned to like what everybody else
does? So there, the commercial model and viability, we waited till the month where we were able to see
that we have enough income. So we have reported in the quarterly earnings that we have actually taken
the all DLG amount that we paid as a cost in the provision, the cost in the quarter and I'm very happy to
say this, that it does not change our profit guideline. We are going to make larger money and this is
going to be helping us net the DLG cost, if at all, any quarter we are assigning in that, and expectedly
every quarter they will be DLG cost and I also want to extend next further that DLG costs, as you are
aware are going to be paid back to us, so higher revenue. So, in a way, the business does not require
additional equity capital or investment because this is in a rotation. Money is in a rotation here.
Alok Srivastava: Okay, sure just a follow up on this, Madhur, this 5% net that you'll be making, is it over
and above the upfront fees that you will make on the loan?
Mr. Madhur Deora, President and Group CFO : It's the total money that we make. So we make a
sourcing fee upfront, we have DLG cost upfront, and then we have collection revenue over time. The
total of all of that, net of the upfront DLG cost that we talked about, will be north of 5% or is expected to
be north of 5%.
Alok Srivastava: Sure and typically, are we talking about a tenor of 12 months or so?
Mr. Madhur Deora, President and Group CFO: Yeah. So the average tenor is about 12 months, I mean,
most of our loans are 12 to 18 months. There can be some which are slightly longer, some which are
slightly shorter but yes, that is in the ballpark of what we do.
Alok Srivastava: Sure, sure, Madhur. That is helpful. Secondly, on net payment margin, I think my
calculation is suggesting some three and a half basis points NPM, that's roughly a basis point
improvement over last quarter. So how has this happened? Has there been some change in mix or
something which has driven this improvement?
Mr. Madhur Deora, President and Group CFO: I won't comment on exactly what the improvement was,
but yes, it has gone up, as we have indicated in our earnings release, that has been due to largely better
monetization of merchants as well as control over our payment gateway costs. So it has been on both
sides.
Alok Srivastava: Okay and should this be the run rate that we should be looking at in coming quarters?
Mr. Madhur Deora, President and Group CFO: Yeah. We do think that we should be able to manage and
we should be able to maintain these sorts of levels, going forward. We do have some quarterly volatility,
maybe because of festive being slightly better, slightly worse and so on and obviously, I'd just like to
point out here that all of these numbers are excluding UPI incentive. So including UPI incentive, for the
year, we expect our payment processing margin to be significantly higher.
Alok Srivastava: Sure, sure. Thanks a lot, Madhur and Vijay. Thanks. All the best.
Mr. Madhur Deora, President and Group CFO: Thank you.
Mr. Vijay Shekhar Sharma, Founder and CEO: Thank you.
Moderator: Thank you. Thank you Alok. Next question is from Aditya Bagdia of Buoyant Capital. Aditya,
you may please unmute your line.
Aditya Bagdia: Yeah. Hi. Thanks for the opportunity and congratulations on a good set of numbers. So
just one question, like you have mentioned in the presentation about increased monetization of the
devices which were not in use. So if you could just highlight your strategy on that and what would be the
rough take rate on those devices right now.
Mr. Madhur Deora, President and Group CFO: So just to be clear, yes, we are focusing on increased
monetization from our devices. The core piece of that, of course, remains subscription revenues and
those subscription revenues have been inching slightly upwards as we get, as we get greater active rates
and so on. We have talked in the release about reactivations but also pick up refurbishment and
redeployments. So we're quite focused on that. So the core of it is subscription revenue. I think we have
given a couple of examples of other places where active devices can also give us increased revenue, and
there have been a couple of examples of that but just to be clear, that relates to active devices, not to
inactive devices.
Aditya Bagdia: Okay. Thanks and what would be the subscription revenues for the quarter, like is there a
change if you redeploy an inactive device?
Mr. Vijay Shekhar Sharma, Founder and CEO: Aditya, the interesting thing is that once we pick up a
device, that merchant does not remain a merchant anymore with us because we picked up the device.
So one number gets reduced there but if we refurb and redeploy the device, we did not incur a capex of
the size of typical capex. We did incur some refurb cost, which in turn signed up a new merchant. So
what we've done and we've written in the detail there, is that we will continue to pick up or recoup the
devices from the market if the merchant is no more using them, refurbish them and redeploy so that is
how we are trying to say we will more monetize the device. I hope I'm detailing it and you can ask which
part I should detail further please.
Aditya Bagdia: Sure Sir, fair enough, fair enough. Thanks a lot. That's all.
Mr. Vijay Shekhar Sharma, Founder and CEO: Thank you.
Moderator: Thank you. Next question will be from Siddharth Gupta, followed by Pranav Gundlapalle of
Bernstein. Siddharth Gupta, Voyager Capital. Can you please unmute your line and ask your question?
Siddharth Gupta: Okay. Hi. I hope I'm audible. Good evening gentlemen, great set of numbers. I have a
couple of questions. Firstly, on the DLG model if you could elaborate on the difference between the take
rate we'd have on non DLG loans and on the DLG loans. Secondly, do we plan on extending this DLG
model to our other lending partners as well and if we have an internal cap that we wish to have on these
kind of models that we have set around Rs 225 crores for this particular lender and, third, I wanted to
understand if we have any plans on, moving back towards a wallet business with a tie up with a potential
bank in the future.
Mr. Madhur Deora, President and Group CFO: So Maybe I'll take the first two questions in which I can
address the wallet question. So, our net take rate, for the DLG business, like I mentioned, should be a
little bit north of 5% over the life of the loan. So when I'm saying net, that is net of DLG cost, that is not
dissimilar to loans which are without DLG. I think the key thing that matters in a loan really is, as you can
imagine, so, you know, interest rates and so on but also what is the credit loss. And that is where, as we
mentioned, we are seeing improving asset quality ever since we restarted doing the merchant loan
business in March and April, so we're seeing improving asset quality that's very encouraging.
Our collection performance is also improving so that is what affects the net take rate but compared to
the two models, which is where your question was Siddharth, they are quite similar. Of course, in the
case of the DLG Model, the DLG cost comes up front. So as this is, once this is ramped up, then it
becomes business as usual. But in the first couple of quarters you will see a bit of a drag, right, and
obviously we have had the numbers that we have had, despite the meaningful amount of DLG that we
have given last quarter.
On your second question, we are open to doing DLG with more partners. I don't think we have a strong
preference one way or the other. Like Vijay mentioned, this is the emerging market practice and we are
perfectly happy to, you know, be in line with what the market practice is. For various reasons, some
lenders may not want a DLG and that is okay as well.
Mr. Vijay Shekhar Sharma, Founder and CEO: Yeah Siddharth, So it's really interesting to know that not
every lender has asked for it but we also wanted to. We are particularly looking at the particular type of
portfolios, etc. etc. so it is not a wider practice that we are going to go with, and that is why we have not
set a limit or a number here either. In other words, we are not saying that it will be on every loan or nor
it is going to be with a cap so that's what we are trying to say.
Siddharth Gupta: But then it leaves me open to the question that apart from, say, signaling to the
lending partners that we are sort of backing up on the quality of the asset that we are bringing to them,
what is our skin, our incentive to kind of go ahead and push forward with this model.
Mr. Vijay Shekhar Sharma, Founder and CEO: I told you a little bit a while back. This has become an
industry practice and regulatory best practice. So our interest was to remain within the borders.
Mr. Madhur Deora, President and Group CFO: And the indication that we have also had from partners is
that their appetite for doing, for the amount of business they do under DLG model is somewhat higher.
So to your point that that signal is not just a sort of qualitative thing, it does actually have an impact on
how much business we do from their standpoint and it is also possible that some new lending partners
may have a preference for DLG model versus maybe, you know, less of a preference of non DLG model.
So our focus is, we're seeing enormous amounts of demand at very good asset qualities and this is a very
profitable business for us. So we do want to try to get into win-win partnerships with other lenders. So if
existing partners can scale more and new and new partners, some potential new partners are finding it
easier to start with this model and continue with this model, then we are open to it.
Siddharth Gupta: Okay, got it and maybe on the wallet bit?
Mr. Vijay Shekhar Sharma, Founder and CEO: Can you ask the question again? Were you asking that you
want to bring the wallet back again?
Siddharth Gupta: Yes, are we envisaging bringing the wallet back with another banking partner, or is it a
product that we've put on the shelf for now, for the foreseeable future?
Mr. Vijay Shekhar Sharma, Founder and CEO: The Paytm wallet was operated by Paytm Payments Bank,
which is under regulatory supervision right now, we would wait for a clear direction on that side first.
Siddharth Gupta: Okay. Thank you.
Mr. Vijay Shekhar Sharma, Founder and CEO: Thank you.
Moderator: Thank you. Next question will be from Pranav Gundlapalle of Bernstein, followed by Rahul
Jain of Dolat Capital. Pranav, you may ask your question now.
Pranav Gundlapalle: Hey. Good evening. I'm just going to go back to the question on DLG. While the
average take rate would be the same versus the earlier arrangement. Would the sensitivity of the
revenue to asset quality change with this model versus the prior model?
Mr. Madhur Deora, President and Group CFO: I think over the last 4 or 5 years since we have started
doing merchant cash advance or merchant loan business, we have seen asset quality in a relatively tight
range, right and obviously, we have disclosed that every quarter, as you're aware. I think within those
ranges, and I would say even give or take a couple of percentage points as much as a couple of
percentage points, on expected credit loss, we don't expect the net take rate to be different or to be
different than what I just mentioned earlier. Right. So the answer is that in all reasonable scenarios, we
don't expect that to be different. In theory, it can be different because it is a little bit more dependent on
collection revenue but, as long as our expected credit losses are in that range or even somewhat higher,
we don't expect the way this model is out is that you will get enough and more collection revenue so
that the net take rate will be, like I mentioned, north of 5%.
Pranav Gundlapalle: Understood, so, yes, I think, you know, in normal circumstances, it probably would
remain the same. I'm just trying to understand, let's say there's zero credit losses for a portfolio. Would
we end up with much higher revenue? Similarly, if there is doubling, would we end up with a much lower
revenue?
Mr. Madhur Deora, President and Group CFO: So if you had zero credit losses, we would expect we
would have much higher revenues, much higher net take rates. If you had even meaningfully higher ECLs,
we would still end up with, through the life of the loan, roughly the same net take rate. Of course, in a
theoretical scenario where we breach, you know, like you mentioned, 2x, then yes, our collection
revenue would be lower but like I mentioned, and it's mentioned in the earnings release as well. The
reason why we are doing this is to release more capital, our lenders are very confident of the business.
We are very confident of the business, we are seeing improving asset quality. Our lenders are committing
more capital on the back of it and the timing, in addition to the regulatory and the market practice, the
timing has been when we feel comfortable that we're not going to have such scenarios.
Pranav Gundlapalle: Understood. Now, I'm just trying to understand the benefit for the partners so that
was the basis of the question. The second question is on your cost base. You've seen, again, a material
reduction this quarter versus last. Would it be fair to say this is a new base or is there room for further
reduction in the near term?
Mr. Madhur Deora, President and Group CFO: At the moment we are guiding to this being the new
base, although we continue to look at our cost base, particularly on people, software costs and other
indirect expenses, which is the largest chunk, about 85% of our other indirect expenses to continue to
find optimization opportunities. I'm optimistic that we will find such opportunities like you may
remember, last quarter we had guided to 5% to 7% for the reduction on the back of full quarter impact
and so on, we exceeded that on employee cost. So we continue to remain very disciplined on trying to
find as many areas as possible and, yeah. So I think that is an ongoing exercise and to find more and
more opportunities, including AI driven opportunities to find efficiencies.
Mr. Vijay Shekhar Sharma, Founder and CEO: Pranav, this is Vijay. I'd like to add a couple of points on
both line items. Important to note that if you notice our contribution margins, they have gone back to
near 55% without any UPI incentive, which is the guidance that we had done with the UPI incentive and
in my belief, this is going to be the new norm. We are very hopeful and sure that it should not cross or go
much lower than these numbers and UPI incentives, sort of what comes out will become on top of it
number one.
Number two, there is one large cost. Pranav, because I love the way you write those notes and I love to
read them, I want to tell you that there is a cloud cost, a pretty large amount of cloud cost and we've
seen one of our industry peers make a cloud in a capex model instead of an opex model and that's
another way to look at the cost structure there. So I personally would operate that as AI comes further
and further, it will become that we are far more profitable on a point to point basis, but we are far more
capital efficient also in using the capital the way this is meant to be. So, I personally remain committed
that technology wise for a per transaction and for per bit of revenue, we should lower cost for people,
lower cost of machines and as you are aware, we are talking AI, which is a little bit of cost, but we would
remain even further cost efficient on that. The models that we are deploying and the cost that we are
incurring on them are phenomenally low.
I'm very happy to tell you we in literally ten months, reduced 60% of our manpower cost on support and
that was so good and this was all triggered by Klarna's blog post that you would have seen out there and
we internally have created AI IVR. You can talk to a machine like it is a human. So interactive IVR
response that used to be front end for the merchants, now there is a single model that is answering
them on a text, and if you want to continue the call, it will continue there and the agent will also know
this. So these are even opportunities to fork out and to be full blown independent technology and
software businesses.
I'm very hopeful, like Madhur is saying, that this is a new norm, that we will be further finding out ways
of our cost, but not necessarily in people, but on an operating cost which are beyond people’s costs. The
point is that, and I also believe that our business with this new DLG model that we've done will bring us
more capital towards credit disbursement to the merchants, and this is more of a future forward
underwriting that our lenders have learned over the period and the quality that they have seen.
Remember, the quality that they saw in last quarters gave us more revenue is the reason that we earned
more credit revenue and more financial services revenue that we've written in the earnings release. So
you're talking about higher margin business getting more excess of growth, opportunity of growth while
the machine based leverage is growing this. So I'm personally hopeful. Let's see what goes up in the
future.
Pranav Gundappe: Understood, that's super helpful. Thanks a lot. All the very best.
Moderator: Thank you Pranav. Next question will be from Rahul Jain of Dolat Capital, followed by Jayant
Kharote of Jefferies. Rahul, you may ask your question now.
Rahul Jain: Yeah. Hi. Firstly, on the personal loan distribution business, when you see things turning
better and the way we would like to grow in this space, and from the revenue recognition point of view,
do you see the take rate to ideally go up by 50 to 100%?
Mr. Madhur Deora, President and Group CFO: Sorry. Can you just repeat the second question? Rahul,
explain that before I answer both questions.
Rahul Jain: Yeah. I'm saying in general, for the total business, do we see the take rate going up by
50-100% in the lending business.
Mr. Madhur Deora, President and Group CFO: So on your first question on personal loan distribution,
we have done a fairly good job of disbursing about Rs 1600 - 1700 Crs last quarter. But we do recognize,
as we mentioned in the release, that we have more work to do. I think we have done a decent job this
quarter of adding some new lending partners, and we do hope to add more lending partners in the next
quarter as well. I think that is critical for us. That scaling the lending partners that we have added last
quarter. All those lending partners are relatively small on the platform right now. As well as, you know,
adding and scaling new partners, that really is the way we want to grow this business. I think we've been
talking about that for the last two quarters. I think once we are able to do that and hopefully in the next
when we're talking a quarter from now, we will have more proof points to show to you. We'll be very
confident of scaling this business because the market opportunity is massive. It's just that, you know, you
have to bring in as much supply as you can and as quickly as you can so that is the key, in terms of, how
does this business scale.
There are other factors, there are other tailwinds that could also exist. We are seeing in some sense
enough demand. Right. So the number of key financial services customers that we had last quarter was
about 6 lakhs. But this one is obviously a subset of that. So there is enough and more demand. I think it
is fair to say that in the early days, us and some of our partners are being quite cautious as well. So there
is an increasing penetration opportunity. Finally, I would say, it is important and it is what it is that we are
going through a very cautious phase of the cycle, as it should be, both for us and our lending partners. So
maybe 6 or 12 or 18 months from now, that sort of overall market backdrop is more supportive.
With respect to your second question, we do expect our lending, or, sorry, financial services revenues to
continue to scale up. On a QoQ basis, we did have a very good quarter on the revenue side, despite the
fact that the volume disbursed, the number of Financial Services customers did not go up very fast, but
we did get better revenues. This does create a base for us to continue to scale it. I think as we get more
volume through our platform on both, Merchant Loans and Personal Loans, we should be able to achieve
that over the next couple of quarters.
Rahul Jain: And just last bit, if I could ask one more, on the ad initiative on the sound box, do we see this
could be a meaningful contributor in the near term basis and what should be the ideal runway?
Mr. Vijay Shekhar Sharma, Founder and CEO: Rahul, I don't think it will be a meaningful contributor. The
intention was to say that we really continue to innovate on the technology and the various aspects of
merchant businesses. This is something that FMCG companies asked us and then Meesho asked us. So
we thought that we would talk about it. Meaningful is a big number. So I'm going to say that these are
one of those 20% experiments that our team continues to do.
Mr. Madhur Deora, President and Group CFO: I would add that, this channel of advertising is a bit of a
differentiator. We would hope that this does scale but these things specifically, this particular channel,
any new channel does take a little bit of time to scale. We also hope that we see, knock-off impact of this
on our overall advertising business that we are able to offer a differentiated, effectively publishing
property to our advertisers and as a result, they advertise they do this, but they also advertise more on
our platform.
Mr. Vijay Shekhar Sharma, Founder and CEO: And we are trying to defend our product actually by
creating more ways to earn revenue per product.
Rahul Jain: Sure. Thank you. That's all.
Moderator: Thank you Rahul. Next question will be from Jayant Kharote of Jefferies, followed by Anand
Dama of Emkay. Jayant you may ask your question.
Jayant Kharote: Thanks, Pranav. This one's for Madhur. Madhur, I just wanted to understand the
accounting for this DLP model. I get it that the net take rate should remain on MLs north of 5%, but the
structure is through the P&L. Should it be like a gross take rate of 10% minus the FLDG cost and the net
take rate? And if that is the case, how many quarters do we take to reach that steady state? Sort of
accounting gross and net numbers.
Mr. Madhur Deora, President and Group CFO: Yeah. So, the sourcing fee is taken up front. The DLG cost
is basis an ECL model. Given this is a new product, we have taken, basis of the ECL model, the entire cost
of DLG has been taken up front. It is in the other direct expenses, so above contribution margin. The
collection revenues will come in under financial services revenue over time. The time period of that, like
we mentioned, the average tenor of these loans is about 12 to 18 months. So the vast majority of that
revenue will come in less than 18 months. Actually, the largest chunk comes in 12 months, but let's say
the vast majority comes in about 18 months. Then there is some tail revenue because you have loans
which may have gone GCL, but you continue to recover those loans even past the full tenor of the loan
or even past the last repayment date so that's sort of the profile. These are not very long dated, but at
least for the next couple of quarters, they create a bit of a drag compared to if we had to do these loans
without DLG.
Jayant Kharote: Just to clarify, 12 months from now, our gross take rate if the ECL is holding up goes to 8
to 10% and net of FLDG we will be at 5%. Of course, it can be better if the recovery is stronger. Is that a
correct understanding, 12 months from now?
Mr. Madhur Deora, President and Group CFO: That's probably correct.
Jayant Kharote: Great and lastly on the costs. Again, phenomenal job guys. I think in two quarters it will
come down to these levels. How do we go from here? Is this now, should we expect quarter on quarter
growth on this, especially the non sales employee cost base or is there more more headroom?
Mr. Vijay Shekhar Sharma, Founder and CEO: I think Jayant primarily you should think of if you were to
expand marketing costs. I mean that too when UPI new customer onboarding and market share cap etc.
show up which I believe that for concentration risk will be done. So in my opinion, once that is taken care
of, we would spend money on marketing and that is the time that you should see this growing. As far as
people are concerned, not really, but I do believe that UPI consumer growth offers an incredibly large
opportunity for us. As you are aware, this business was earlier not being done by OCL, but by our
associate, PPBL. Thanks to RBI and NPCI, they allowed us to become a player as OCL and now we are
awaiting new customer additions and once that is allowed, we would spend on marketing, but albeit
only large when we will take care of market share cap also. So you are expecting the increase only at a
materially changing market condition. Not otherwise.
Jayant Kharote: Great and if I could just squeeze one last one. On the active sales employees, I see that
that base is stabilizing at around 30,000 - 31,000. Given that you are doing a lot of redeployment of
devices, should we expect this number to grow moderately rather than going back to that 35,000 -
40,000 number?
Mr. Vijay Shekhar Sharma, Founder and CEO: We are also enhancing the productivity per employee,
behind the scene. Let me also say the AI that we keep singing a song of is also going to help us on per
employee productivity in the sales field. So while the number would increase slowly, there will be further
productivity enhancement rather.
Jayant Kharote: Great, and congrats guys for the great set of numbers.
Mr. Vijay Shekhar Sharma, Founder and CEO: Thank you so much. Thank you.
Moderator: Thank you Jayant. Next question is from Anand Dama of Emkay followed by Suresh
Ganapathy. Anand, you may ask your question.
Anand Dama: Hey, thank you and congratulations for a great set of numbers. Is it possible for you to
quantify what the collection revenue that included in the, you know, financial services?
Mr. Madhur Deora, President and Group CFO: We don't really break that out historically, and I would be
reluctant to sort of put out another data point. But we have mentioned earlier that 3.5% - 4% historically
was the sourcing revenue and roughly 1%, and maybe in some quarters slightly more, is the collection
revenue so that's broadly the split on obviously the non FLDG model and non-distribution model. So not
the loan distribution only, which obviously doesn't have the collection revenue. In the last quarter it was
slightly higher in terms of that split, because we did a really good job of repayments and collections and
like we had mentioned, just merchants are just using mobile payments more so that helps the overall
performance of the merchant lending business. So it was slightly higher, so that's about as much
direction as I could give you.
Anand Dama: For sure. And this is primarily on the Merchant loans and Personal loans business both
right put together ?
Mr. Madhur Deora, President and Group CFO: Well, actually it's the merchant loan. Because on the
merchant loans, just to remind you we are doing the same model we've been doing over the last 4 or 5
years, obviously now in part with FLDG also. In the personal loan business, the vast majority of our
business over the last 2 - 3 quarters has been a distribution only model. So there is really no collection
arrangement. Our lending partners do their own collection.
Anand Dama: And any update on the new loan products that we are talking about earlier on, like you
know, home loans, mortgages and stuff?
Mr. Madhur Deora, President and Group CFO: I think there are a few experiments and integrations
going on with a few secured products. I don't think that at this point, in the financial services business,
that is our number one priority, because we see a big penetration opportunity in both merchant lending
and personal loans. Like we mentioned earlier, in merchant loans, there's a huge amount of demand and
we just want to unlock more capital, including through these DLG arrangements and on personal loans,
the focus is on adding more and more partners so that is really the core focus of financial services. While
we have work going on, I think you should really look at that as maybe having some meaningful
contribution after the next 2 or 3 quarters, as opposed to any time very soon.
Anand Dama: And lastly, is there anything pending from our side to be done for the NPCI to approve the
new user or customer onboarding?
Mr. Vijay Shekhar Sharma, Founder and CEO: Hi, this is Vijay. So as of now nothing seems like it. We are
just in a wait and watch state. I wish we can start sooner.
Anand Dama: Thank you.
Moderator: Thank you Anand. Next question will be from Suresh Ganapathy of Macquarie, followed by
Nitin Agarwal from Motilal Oswal. Suresh, you may please ask your question.
Suresh Ganapathy: Yeah. Thanks. So, Madhur, sorry, just a little bit more on this FLDG thing. So if you
have about Rs 1600 crores of portfolio, which is under the FLDG, and let's assume you are giving 5%. So
you are saying that 80% is given in the form of bank guarantee, and there is a cost associated with that
bank guarantee and apart from that, a certain ECL cost which has been expensed through the P&L. Is my
understanding right?
Mr. Madhur Deora, President and Group CFO: No. Sorry. That's, let me just clarify. Suresh, so Rs 1650
crores is the AUM, as of September 30th. The disbursed amount is slightly higher than that, as you would
expect, because some installments have already started, and have been repaid. So the disbursed amount
is slightly higher than that. On that amount, the arrangement is that we give a DLG. The DLG is not 5% it
is meaningfully lower than 5%. 5% is the cap, as you obviously know from the regulator. So our DLG is
significantly lower than that. There is no bank guarantee here, although there is flexibility to give it as a
bank guarantee under regulation. Our arrangement is that, in this case we would most likely give this as
a FD, which would be lien marked, and all of that cost, 100% of the DLG that we give, the arrangement is
that we most likely give that in the form of a FD, and that FD would be lien marked, and that entire
amount of DLG that we are giving in the form of lien marked FD, has been expensed in the last quarter.
So in other words, there is no DLG given which is not expensed in the P&L this quarter.
Suresh Ganapathy: Okay. Okay. So just to understand the numbers, let's assume it is Rs 1500 crores and
the disbursement is higher and 2% is what you have given. That means you are saying 30% has been
expensed, Rs 30 crores has been expended to the P&L. I'm just telling the ballpark, just a rough
calculation.
Mr. Madhur Deora, President and Group CFO: That's right. Yeah.
Suresh Ganapathy: Okay, so Rs 30 crores has been fully expensed to the P&L and it is coming in the
other direct expenses, right?
Mr. Madhur Deora, President and Group CFO: Exactly.
Suresh Ganapathy: Okay. Let's hypothetically assume that the number is 5%. The actual experience of
that client is 5%. So effectively, we are saying that instead of Rs 30 crores, it's closer to say Rs 60 - Rs 70
crores. What happens with the remaining Rs 30 crores? Who bears the hit? The company bears the hit or
what happens to Paytm? Is there a clawback arrangement? Because you have only expensed till Rs 30
crores, right? Just throwing numbers off the air but just to understand the mechanism.
Mr. Madhur Deora, President and Group CFO: Sure, so let me just simplify the numbers because they're
all illustrative anyway. Let's say we do Rs 100 crores of disbursal and let's say we have 3% DLG. Okay. So
though that Rs 3 crores will be given in the form of FD. That entire three crores will be expensed. Now,
let's say the GCL is higher than 3% or higher than three crores on that book of Rs 100 crores. All of that
hit is credit loss for the partner. So in this case, because we have publicly disclosed, I can say in this case
where we have given DLG, we're talking about SMFG, where we have given a separate disclosure. And
that is a part of their P&L. Because obviously they're making interest income as well. And on the
remaining 95% or 97% of loans, which are good, so they're making interest income on that, even net of
that additional 2% or 3% whatever we are talking about here, they have very good RoA, right. So it is a
DLG. In this case the first 3% as we were using in our illustration, the first 3% gets offset against the FD.
After that, all the hit is passed on. And then on top of that, depending on the performance of the book,
we also make what we expect to be a significant amount of collection revenue. But that over the life of
the loan.
Suresh Ganapathy: But if it crosses 3%, how can they give you a collection incentive? Because you have
already crossed the FLDG limit. And the company is not happy with the number being crossed 3%. You
will still get a collection incentive if the GCLs are higher than 3%?
Mr. Madhur Deora, President and Group CFO: Yes. So, let's extend that same example. So we have Rs
100 crores of disbursal. We have 3% DLG and let's say the partner has, let's say the book eventually ends
up at 5% NCL. So the partner now has Rs 5 crores of credit cost. They get Rs 3 crores from us. And on
that performance level, over the life of the loan, Paytm would not only not have any additional cost to
the partner, we will also make significant collection revenue from the partner.
Suresh Ganapathy: Okay. So this is clear. But just one final question, because this is an important thing
for all of us to understand. Now the RBI is very clearly telling us, as per the rules and regulations, both
synthetic FLDG and non synthetic structures like collections will be taken as a part of the overall 5% limit.
Somewhere down the line we are saying this collection is not a non synthetic FLDG because the RBI may
view it as a non-synthetic FLDG, right?
Mr. Madhur Deora, President and Group CFO: I cannot speculate on that Suresh. Honestly, we have
gone through extreme rigor to ensure that this is in alignment with the regulations, alignment with
market practices, of course, and to the satisfaction of compliance teams of both sides. So the collection
arrangement that we have is very much permitted, and it isn't what you may call a synthetic DLG. We are
not in the business of giving synthetic DLGs.
Suresh Ganapathy: Okay. This is pretty clear. Thank you so much, Madhur.
Mr. Madhur Deora, President and Group CFO: Thank you. Please feel free to reach out with any other
questions.
Suresh Ganapathy: Sure. Yeah.
Mr. Madhur Deora, President and Group CFO: Thank you. Suresh.
Moderator: Thank you. Next question is from Nitin Aggarwal and this will be the last question for today.
Nitin, you may ask your question.
Nitin Aggarwal: Yeah. Hi. Thanks for the opportunity. Good evening everyone. So two questions. One is
like, what do you plan to do with the cash on the balance sheet now that it has increased after the sale
of the business and what is the optimal number you would like to carry for your new requirements in
terms of cash?
Mr. Madhur Deora, President and Group CFO: I think Nitin, we want to address and visit that question
with our board. I think one of the things that we have decided is we want to be consistently free cash
flow positive, which is not that far away from for us now before we take that decision, to the board and
come up with a sort of a firm guidance, or not. I mean, firm guidance, as in a directional framework for
what we think of as excess cash, how do we think about returning that cash and of course before that,
what are the uses of that cash? So yes, we have talked about this. This does come up on nearly every
quarterly call and I do acknowledge that we have Rs 10,000 crores of cash, and I don't see any scenario
under which we will be able to use up any meaningful percentage of that cash. But I think we have
decided that let's get to the the most important thing is that business should throw off cash. Right and
we feel like we're getting close to that and we'll absolutely address that with our board and hopefully
have a better answer for you once we have crossed that milestone.
Nitin Aggarwal: Sure Madhur, And the other question is like, if I look at in metros and key cities, there is
already a good coverage of digital payment provisions there at almost all merchants will be something
that will be like signing merchants. So what is the TAM that you really look at? Is the growth in
merchants coming in more from suburban regions or say like going one level down metros and both in
numbers, I mean, as well as in the value in terms of GMV. What is the TAM that you are really looking at?
Mr. Vijay Shekhar Sharma, Founder and CEO: Hi, this is Vijay and while we all see significant amount of
Paytm and Paytm soundboxes all around us in metro cities, I am going to surprise you by saying that the
penetration scope is nearly double of what it is penetrated as of now in metro cities, I'm talking metro
cities only. So we are talking about a significant amount of TAM in the metro cities themselves. Possible
and the reason that metro cities I'm talking about is because there is a consumer merchant network
effect, because more metro city consumers pay using smartphones, mobile payments, the more
merchants need soundbox number one.
Number two, what we are seeing in metro cities and a little bit ahead, let's say top 10 cities or top 20
cities is that merchants now do not wait for a larger percentage of QR based payment, Paytm QR based
percent payments. They are starting to take a soundbox very early in the journey of being onboarded
itself. So here, I mean, numbers can be very comfortable. I mean, NPCI gave about 60 million merchant
data, although I do not know the uniqueness check etc on that data but I can say that there is a market
of tens of million more sound boxes out there.
Nitin Aggarwal: This is very interesting and lastly, just as a data point, how many inactive devices do we
have any plan to pick from merchants? How much is that number?
Mr. Vijay Shekhar Sharma, Founder and CEO: We don't. So nothing of sort of that we know that this is
the inactive merchant. We are trying to go activate the merchant, and we say the device is not working
or picking up because of that. So it's an ongoing journey. What I can only tell you one thing here is that
we found out that these devices, which we are picking back from the market, are more like battery
outage or some plastic refurbishments, etc. we see which is not very large. So the keyword is that there
you go with the opportunity of picking them back and then installing refurb devices back. So merchants
become active, revenue starts coming back so that is why you are seeing there is a larger amount of TAM
out there.
Nitin Aggarwal: Got it. Thank you so much and wish you all the best.
Mr. Vijay Shekhar Sharma, Founder and CEO: Thank you, thank you.
Moderator: Thank you. Next question will be taken from Sachin Salgaonkar. Sachin, you may ask your
question.
Sachin Salgaonkar: Thanks Pranav Apologies. I signed up late. So if any of these questions is answered.
Sorry about that in advance. First question, just wanted to understand how fast we could see the wealth
insurance business growing and what are some of the new areas which you guys are exploring in terms
of secured lending and any color you could provide that would be helpful.
Mr. Vijay Shekhar Sharma, Founder and CEO: Sachin, first of all, secure lending or the loans which are of
low margin, etc., we've learned that everything ends up becoming the book for lenders and if we are
assigning secure lending distribution also on the same side of disbursement allocation, we rather lose an
opportunity of another high, better product for the customers. So we are not doing a large amount of
secure lending and that is one of the big factors, by the way, that personal loan disbursements were sort
of not in line with what somebody would have expected. So in other words, we are not aggressively
going after secure loans. Let's say that and then I personally suggested that this is something that we will
look at later, if at all we need to look at.
Then when you talk about wealth and insurance, the good thing is that these things, especially the
wealth market, have had a tailwind. Where there is a great amount of opportunity happening and
opportunity coming in. But when you look at insurance, there is a distribution that we are working on,
are they going to become materially important. That is exactly the reason if you notice, we have started
to give number of transacting users or number of, financial services customers because overall the
business model will look like payment customers and cross-sell to them and cross-sell per customer will
be the revenue because disbursements or GWP or whatever we help distribute won't be the primary
number, but the revenue per customer is what we are headed behind the scene so yes. We don't expect
them in 1 or 2 quarters, but do expect them in due course, let's say second quarter. Third quarter
onwards showed up as better than today's contributions and that is why we are trying to say financial
services at large matters, not just credit distribution.
Sachin Salgaonkar: Thanks Vijay, very clear.A quick follow up out here. So from a loan perspective, is it
only the merchant loan book which would materially scale up, let's say in the foreseeable future?
Mr. Madhur Deora, President and Group CFO: I think we see opportunities in both merchant and
personal loans. I think the demand side of it, the ability to do very, very sensible business in both of
those is enormous. I think the dynamics are slightly different. Where in merchant loans you know, I think
the growth of our devices business, after some interruptions that we had earlier this year, is now
creating that ramp up. On personal loan, I think, we did talk about this a little bit earlier, but I'm happy to
repeat, that one of the key things that we had talked about over the last two quarters is adding new
partners. So we're pleased to say that we did add some new partners this quarter, but quite frankly,
they're not ramped up yet and we do have other partners in the pipeline as well. So we need to get the
new partners as well as potential new partners, integrated and ramped up and that will create the
opportunity. There's no dearth of demand. It is just that we have to create more supply on the platform.
Sachin Salgaonkar: Very clear. Thank you. Thank you. Second question, I just wanted to understand a bit
more on your what kind of steady state EBITDA margin should we expect from the business, particularly
given the fact that business model has evolved a bit after some interruptions?
Mr. Madhur Deora, President and Group CFO: Yeah, I don't think we should necessarily give that
guidance right now. We have talked about, which I talked about last quarter, about being profitable, in,
by having one profitable quarter by the end of the year and despite the DLG costs that we talked about
earlier in the call, we expect to not only meet that guidance but exceed that guidance. So deliver some
significant profitability this year and then with all the tailwinds that we have, especially on merchant
payments, merchant lending, personal loans, and the huge improvements that we have had in our cost
structure, we expect to get very meaningfully profitable. So we are seeing this as getting to very
meaningful profitability relatively soon, becoming a business that is throwing off cash. But specific
EBITDA margin range I'd rather not get into.
Sachin Salgaonkar: Okay. Thanks and my last question Madhur is just on any thoughts on potential cash
return back to shareholders, to your comments about, you know, trying to get into a cash position very
soon. There's a guidance of EBITDA breakeven by, let's say, 3Q or 4Q and potentially at some point, you
know, as and when the PayPay IPO happens, there could be, you know, incremental cash, which you guys
could end up getting. So if you add it all together, do we see some kind of a potential cash return to
shareholders? Maybe not immediately, but at some point in the next 12 to 18 months.
Mr. Madhur Deora, President and Group CFO: Yeah. I think your observation is right that we do have
more cash than we need for any organic or inorganic opportunities and we do expect to get back in a
position where we are generating cash. This question was asked about 10 or 15 minutes ago, by Nitin
from Motilal Oswal. I think we want to get to a position where we are sustainably throwing off cash and
then have a, you know, a very good robust framework with the board about how we think about the
cash balance, use of money, as well as use of excess money. So hopefully in a couple of quarters I'll have
a better answer to this.
Sachin Salgaonkar: All right. Thank you.
Mr. Vijay Shekhar Sharma, Founder and CEO: I also, I would also add on behalf of, overall a board
discussion that we had that we need to be fairly long haul in generating free cash before we start to
think about returning it to the shareholders. There should be a trigger or a reason for it and right now,
these cash amounts that we are able to get, we are rather going to be focused on operating business and
higher margin and more revenue and more profit.
Sachin Salgaonkar: Thanks. Very clear Vijay.
Mr. Vijay Shekhar Sharma, Founder and CEO: Thank you.
Moderator: Thank you. Next question will be from Vijit Jain of Citi and this will be the last question for
today. Vijit you may go on and ask your question.
Vijit Jain: Yeah, thanks. And sorry I joined late. So if this is a repeat, my apologies. My first question is,
within the merchant loans business going forward, what kind of share do you think DLG will take as a,
you know, in terms of disbursements going forward? Are you looking at a mix in mind? That's my first
question.
Mr. Madhur Deora, President and Group CFO: Vijit, we, honestly, that's not a metric. We have gone
through and we'll share the transcript with you. We've gone through the DLG economics in some detail
earlier in the call, as you would imagine. But in summary, over the life of the loan, we see this business
as very profitable. We see, you know, regulatory clarity on this. We see certain lenders having a
preference for this and of course, we see a huge amount of demand and this is very like I said, this is a
very profitable business for us, with or without DLGs. Right? So when you look at it from that prism, we
are perfectly okay for business to be done on DLG model going forward and I don't think there is a metric
that we're trying to manage to do x percent should be DLG and x percent should be non DLG and we're
going to find out more in the next few quarters whether it stabilizes to a certain number, in which case
we can start talking about, hey, what do we expect but we're certainly not managing to a number.
Vijit Jain: And my next question is going to be, you know, are there any major areas within, payments or
financial services that you think you could still venture into. I know I've asked this question before, but,
once you get the RBI payment gateway license, does that open up things like cross-border? Is that
meaningful? Is that something that you would like to do? That's my first question and, if you can just
comment on if there's a timeline on when you get RBI license and also on the NPCI side. Thank you.
Mr. Vijay Shekhar Sharma, Founder and CEO: Thank you Vijit. This is Vijay, and I'm taking this question.
So number one. Yes, that is one of the big reasons that I'm personally, whenever this discussion of
returning capital to the shareholders comes up, I am suggesting that there are tremendous opportunities
for Paytm to grow within the current framework. First and foremost, let's go back to the moment when
Paytm Bank originated. We gave the wallet to the bank. We transferred the bill payment business to the
bank, and in due course, the UPI also was operated by the bank. Being at arm's length and being at a
different entity, the payment bank had its own business priorities and instead of growing UPI market
share, it probably focused on other business models. So consumer side UPI market share for Paytm
Payments Bank was something that we all know was not in the range of what other apps were showing.
While when you look at Paytm operated Wallet or Paytm operated QR, Paytm operated different
services, we were the market leader there very clearly and are the market leader very clearly.
Now, the consumer base of UPI is an opportunity which is way bigger than what we anticipate in a
conversation as of now. Remember, the UPI consumer for Paytm is an open and wide open opportunity.
The product, technology, market ownership, customer ownership, everything belongs to Paytm, and I
really thank RBI and NPCI for making this possible and partner banks that as Paytm we are able to get
these consumers. So Vijit think about right now RBI asked and Paytm Bank transferred 130 million
customers plus 200 million handles to OCL and now once NPCI will give us a confirmation, we will be
able to grow and my friend, I'm telling you, we are not in this to become a mediocre player or remain a
fringe player.
We are here to solve the problem of concentration risk or a market share, and we remain that
aggressively committed towards consumer payment like you've seen us committed towards merchant
payments. So the very fact that Paytm will have an opportunity to play in UPI consumer market share will
be an extraordinarily large opportunity. As you can guess, once we have the customer on our platform,
ownership of our customer customers on our platform, we will be able to grow tons of cross-sell of
financial services to this consumer and then obviously there are byproducts like marketing services and
advertising, etc. that you're talking about. And remember, in the UPI ecosystem, when RBI allowed us to
become a TPAP player, it very clearly marked us a responsibility to Paytm that we will be able to
potentially solve for concentration risks that the system carries.
As an Indian player, as a pioneer of the mobile payment system in India, we remain committed and we
remain committed to invest and expand our offering. So remember, as an Indian player, as India's
homegrown champion, we are here to invest in payments and there is a tremendous large amount of
opportunity in consumer payments. When you come about the merchant side, as a PA license, you
should know that online payment innovations are something that we were able to bring QR on a desktop
so that the customers' higher trust, less fraud prone and superior payment checkout systems happened.
Since two years we've not acquired new consumers, but we have built a dramatically large amount of
technologies, including cross border multi-currency, including quick commerce which requires many
other payment products.
We are waiting to onboard as many more merchants so that we can onboard newer quality products and
offering to those customers. And I'm very happy to tell you, Vijit, you could figure out for yourself these
foreign transfers, including another service such as omnichannel payments systems, have very
impactfully showed up in the market right now. Imagine Tanishq is a customer for us offline, let's say, but
they are not online. For us, we are not able to build an omnichannel payment and India has to lead the
way in payments. I do believe that extraordinary amount of opportunity in payments for us to grow a
larger TAM. What we are right now focused, as you could see, is monetization and we are showing the
market that we can very well optimize and monetize and in due course we will, when we get an
opportunity, we will expand the TAM of the consumer and merchant both together.
Vijit Jain: Great. Thank you so much Vijay, and best of luck with everything and hope you guys have a
really good festive Diwali ahead. Thank you so much.
Mr. Vijay Shekhar Sharma, Founder and CEO: Thank you. Thank you and thank you everybody for joining
us. Wish you all a very happy Diwali festive season and your support means a lot to us and see you again
after Diwali.
Mr. Madhur Deora, President and Group CFO: Yes, Bye.
Moderator: With that, we come to an end of this call. A replay of this earnings call and the transcript will
be made available on the company website subsequently. Thank you all for joining, you may now
disconnect your lines.
Mr. Vijay Shekhar Sharma, Founder and CEO: Thank you. Bye.
"""
    company_name = "Paytm"
    gem = GeminiRunner()
    res = gem.generate_summary_response(context= context, company_name= company_name)
    print(res)