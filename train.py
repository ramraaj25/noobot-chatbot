from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import logging

# Custom response selection method


def get_latest_response(input_statement, response_list, storage=None):
    """
    :param input_statement: A statement, that closely matches an input to the chat bot.
    :type input_statement: Statement

    :param response_list: A list of statement options to choose a response from.
    :type response_list: list

    :param storage: An instance of a storage adapter to allow the response selection
                    method to access other statements if needed.
    :type storage: StorageAdapter

    :return: Return the first statement in the response list.
    :rtype: Statement
    """
    logger = logging.getLogger(__name__)
    logger.info('Selecting first response from list of {} options.'.format(
        len(response_list)
    ))
    return response_list[len(response_list) - 1]


bot = ChatBot(
    'NooBot',
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    read_only=True,
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "default_response": 'I am sorry, but I do not understand.',
            "response_selection_method": get_latest_response,
        }
    ],
    database_uri="sqlite:///noobot.db"
)


if __name__ == "__main__":

    # trainer = ChatterBotCorpusTrainer(bot)

    # trainer.train('chatterbot.corpus.english')
    # print('training complete')

    list_trainer = ListTrainer(bot)

    list_trainer.train([
        # List of statements here
    ])
