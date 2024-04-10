class APIConstants(object):
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # Update, PUT, PATCH, DELETE - bookingId
    def url_patch_put_delete(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

    def url_get_all_booking(self):
        return "https://restful-booker.herokuapp.com/booking"