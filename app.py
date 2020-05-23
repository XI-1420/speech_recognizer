from util import utils
from speech_converter import speech_to_text
from grammar_rater import rate_spelling
from grammar_rater import rate_unnecessary_fillers
from grammar_rater import rate_grammar
import time
import asyncio

filename = "speech.txt"


async def main():

    if speech_to_text(filename):
        
        loop=asyncio.get_running_loop()
        data = utils.read_file(filename)
        words_count = utils.total_words(data)
        print("="*44)
        print("total spoken words                   -> ", words_count)
        print("="*44)

        fut_speech_fluency=loop.create_future()
        loop.create_task(utils.rate_speech_on_fluency(fut_speech_fluency,words_count))
        fluency_rating = await fut_speech_fluency

       
        spelling_rating = rate_spelling(data, words_count)

        fut_unnecessary_filler=loop.create_future() 
        loop.create_task(rate_unnecessary_fillers(fut_unnecessary_filler,data))
        filler_rating = await fut_unnecessary_filler
        
        grammar_rating = rate_grammar(data)
        
        print("="*44)
        print("fluency rating             (out of 1)-> ", fluency_rating)
        print("spelling rating            (out of 2)-> ", spelling_rating)
        print("unnecessary fillers rating (out of 1)-> ", filler_rating)
        print("grammar rating             (out of 1)-> ", grammar_rating)

        total_rating = fluency_rating + spelling_rating + filler_rating + grammar_rating
        print("="*44)
        print("overall rating             (out of 5)-> ", total_rating)
        print("="*44)
    
asyncio.run(main())

