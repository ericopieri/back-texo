from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Producer
from core.serializers import ProducerSerializer


class MaxMinIntervalWinnerProducerView(APIView):
    def get(self, request, format=None):
        producers = Producer.objects.all()

        if producers.count() == 0:
            return Response(
                {"mensagem": "Nenhum produtor encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )

        max_interval_winners_producer = []
        min_interval_winners_producer = []

        max_interval = -1
        min_interval = float("inf")

        for producer in producers:
            interval_data = producer.calc_win_interval()
            interval = interval_data.get("interval")

            if interval is not None:
                if interval > max_interval:
                    max_interval = interval
                    max_interval_winners_producer = [producer]
                else:
                    if interval == max_interval:
                        max_interval_winners_producer.append(producer)

                if interval < min_interval:
                    min_interval = interval
                    min_interval_winners_producer = [producer]
                else:
                    if interval == min_interval:
                        min_interval_winners_producer.append(producer)

        return Response(
            {
                "max": [
                    {
                        "producer": ProducerSerializer(winner).data.get("name"),
                        **winner.calc_win_interval(),
                    }
                    for winner in max_interval_winners_producer
                ],
                "min": [
                    {
                        "producer": ProducerSerializer(winner).data.get("name"),
                        **winner.calc_win_interval(),
                    }
                    for winner in min_interval_winners_producer
                ],
            },
            status=status.HTTP_200_OK,
        )
