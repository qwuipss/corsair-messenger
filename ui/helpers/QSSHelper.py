class QSSHelper:

    @staticmethod
    def font_size(font_size: int):

        if not isinstance(font_size, int):
            raise TypeError(type(font_size))
        
        return f"font-size: {font_size}px;"

    @staticmethod
    def border_radius(border_radius: int):

        if not isinstance(border_radius, int):
            raise TypeError(type(border_radius))

        return 
        f"""
            border-top-left-radius: {border_radius}px;
            border-top-right-radius: {border_radius}px;
            border-bottom-left-radius: {border_radius}px;
            border-bottom-right-radius: {border_radius}px;
        """

    @staticmethod
    def background_color(hex_color: str):

        if not isinstance(hex_color, str):
            raise TypeError(type(hex_color))

        return f"background-color: {hex_color};"

    @staticmethod
    def color(hex_color: str):

        if not isinstance(hex_color, str):
            raise TypeError(type(hex_color))

        return f"color: {hex_color};"