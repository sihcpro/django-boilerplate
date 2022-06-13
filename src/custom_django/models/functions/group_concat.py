from django.db.models import Aggregate, CharField


class GroupConcat(Aggregate):
    function = "GROUP_CONCAT"
    template = (
        "%(function)s(%(distinct)s%(expressions)s%(ordering)s%(separator)s)"
    )
    allow_distinct = True

    def __init__(
        self, expression, distinct=False, ordering=None, separator=",", **extra
    ):
        super(GroupConcat, self).__init__(
            expression,
            distinct="DISTINCT " if distinct else "",
            ordering=" ORDER BY %s" % ordering if ordering is not None else "",
            separator=' SEPARATOR "%s"' % separator,
            output_field=CharField(),
            **extra
        )


# Example:
# LogModel.objects.values('level', 'info').annotate(
#     count=Count(1),
#     time=GroupConcat('time', ordering='time DESC', separator=' | ')
# ).order_by('-time', '-count')
