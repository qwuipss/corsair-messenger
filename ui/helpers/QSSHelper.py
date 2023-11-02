class QSSHelper:

    @staticmethod
    def concat(*styles: str) -> str:
        return ' '.join(styles)

    @staticmethod
    def font_weight(weight: int) -> str:

        if not isinstance(weight, int):
            raise TypeError(type(weight))
        
        if not 1 <= weight <= 1000:
            raise ValueError(weight) 
        
        return f"font-weight: {weight};"

    @staticmethod
    def border_none() -> str:
        return "border: none;"

    @staticmethod
    def width(width: int) -> str:

        if not isinstance(width, int):
            raise TypeError(type(width))
        
        return f"width: {width}px;"
    
    @staticmethod
    def min_height(height: int) -> str:

        if not isinstance(height, int):
            raise TypeError(type(height))
        
        return f"min-height: {height}px;"
    
    @staticmethod
    def font_size(font_size: int) -> str:

        if not isinstance(font_size, int):
            raise TypeError(type(font_size))
        
        return f"font-size: {font_size}px;"
    
    @staticmethod
    def font_family(font_family: str) -> str:

        if not isinstance(font_family, str):
            raise TypeError(type(font_family))

        return f"font-family: {font_family};"
    
    @staticmethod
    def border_radius(border_radius: int) -> str:

        if not isinstance(border_radius, int):
            raise TypeError(type(border_radius))

        return f"border-radius: {border_radius}px;"

    @staticmethod
    def background_color(hex_color: str) -> str:

        if not isinstance(hex_color, str):
            raise TypeError(type(hex_color))

        return f"background-color: #{hex_color};"

    @staticmethod
    def border_side(side: str, style: str) -> str:

        if not isinstance(side, str):
            raise TypeError(type(side))

        if not isinstance(style, str):
            raise TypeError(type(style))

        return f"border-{side}: {style};"

    @staticmethod
    def background(style: str) -> str:

        if not isinstance(style, str):
            raise TypeError(type(style))

        return f"background: {style};"
    
    @staticmethod
    def padding(top: int, right: int, bottom: int, left: int) -> str:

        if not isinstance(top, int):
            raise TypeError(type(top))
        
        if not isinstance(right, int):
            raise TypeError(type(right))
        
        if not isinstance(bottom, int):
            raise TypeError(type(bottom))
        
        if not isinstance(left, int):
            raise TypeError(type(left))

        return f"padding: {top}px {right}px {bottom}px {left}px;"

    @staticmethod
    def color(hex_color: str) -> str:

        if not isinstance(hex_color, str):
            raise TypeError(type(hex_color))

        return f"color: #{hex_color};"
    
    @staticmethod
    def letter_spacing(spacing: int) -> str:
        
        if not isinstance(spacing, int):
            raise TypeError(type(spacing))

        return f"letter-spacing: {spacing}px;"