from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Producer
from core.serializers import ProducerSerializer


class MaxMinIntervalWinnerProducerView(APIView):
    def get(self, request, format=None):
        producers = Producer.objects.all()

        if len(producers) == 0:
            return Response(
                {"mensagem": "Nenhum produtor encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )

        max_interval_winners_producer = []
        min_interval_winners_producer = []

        max_current_interval = -1
        min_current_interval = float("inf")

        for producer in producers:
            max_interval_data = producer.calc_max_win_interval()
            max_interval = max_interval_data.get("interval")

            min_interval_data = producer.calc_min_win_interval()
            min_interval = min_interval_data.get("interval")

            if max_interval is not None and min_interval is not None:
                if max_interval > max_current_interval:
                    max_current_interval = max_interval
                    max_interval_winners_producer = [producer]
                else:
                    if max_interval == max_current_interval:
                        max_interval_winners_producer.append(producer)

                if min_interval < min_current_interval:
                    min_current_interval = min_interval
                    min_interval_winners_producer = [producer]
                else:
                    if min_interval == min_current_interval:
                        min_interval_winners_producer.append(producer)

        return Response(
            {
                "max": [
                    {
                        "producer": ProducerSerializer(winner).data.get("name"),
                        **winner.calc_max_win_interval(),
                    }
                    for winner in max_interval_winners_producer
                ],
                "min": [
                    {
                        "producer": ProducerSerializer(winner).data.get("name"),
                        **winner.calc_min_win_interval(),
                    }
                    for winner in min_interval_winners_producer
                ],
            },
            status=status.HTTP_200_OK,
        )
