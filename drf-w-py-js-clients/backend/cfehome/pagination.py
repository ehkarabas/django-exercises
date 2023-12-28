from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class LinkHeaderPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        next_url = self.get_next_link()
        previous_url = self.get_previous_link()
        headers = {}
        if next_url is not None:
            headers["Link"] = f'<{next_url}>; rel="next"'
        if previous_url is not None:
            if "Link" in headers:
                headers["Link"] += f', <{previous_url}>; rel="prev"'
            else:
                headers["Link"] = f'<{previous_url}>; rel="prev"'

        response_data = {
            "count": self.page.paginator.count,
            "links": {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
            },
            "results": data,
        }
        return Response(data=response_data, headers=headers)
