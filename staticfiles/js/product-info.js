$(document).ready(function () {
    adjustFontSize();

    $(window).resize(function () {
        adjustFontSize();
    });

    function adjustFontSize() {
        $(".product-name a").each(function () {
            const $productInfo = $(this).closest(".product-info");
            const maxWidth = $productInfo.width();
            const $text = $(this);

            const maxFontSize= 24;

            $text.css("font-size", "16px");

            for (let fontSize= 16; fontSize <= maxFontSize; fontSize++) {
                $text.css("font-size", fontSize + "px");
                if ($text.width() <= maxWidth) {
                    break;
                }
            }
        });
    }
});
