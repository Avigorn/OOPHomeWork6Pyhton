from small_data.Stream import Stream


class StreamComparator(Stream):

    @staticmethod
    def compare(o1: Stream, o2: Stream) -> int:
        result_of_comparing = o1.getStreamID().compare_to(o2.getStreamID())
        if result_of_comparing == 0:
            result_of_comparing = o1.getStreamName().compare_to(o2.getStreamName())
        if result_of_comparing == 0:
            return result_of_comparing