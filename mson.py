

class Mson:

    def to_json(query_output):
        retobj = []
        retval = query_output
        for peer in retval:
            retobj.append({
                'name': peer.name,
                'email': peer.email
            })
        return retobj