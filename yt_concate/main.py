from yt_concate.pipeline.steps.get_vedio_list_from_channel import GetVedioList
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.postfight import Postflight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        Preflight(),
        GetVedioList(),
        DownloadCaptions(),
        Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
