title: Curriculum Vitae
date: 2014-01-12 13:00

Source: [https://github.com/adrinjalali/cv/blob/master/adrin-jalali.pdf](https://github.com/adrinjalali/cv/blob/master/adrin-jalali.pdf)
<!-- really dirty! this is just a test drive ;) -->

<script type="text/javascript" src="https://raw.github.com/mozilla/pdf.js/gh-pages/build/pdf.js"></script>
<script type="text/javascript">
function renderPDF(url, canvasContainer, options) {
    var options = options || { scale: 1.5 };
        
    function renderPage(page) {
        var viewport = page.getViewport(options.scale);
        var canvas = document.createElement('canvas');
        var ctx = canvas.getContext('2d');
        var renderContext = {
          canvasContext: ctx,
          viewport: viewport
        };
        
        canvas.height = viewport.height;
        canvas.width = viewport.width;
        canvasContainer.appendChild(canvas);
        
        page.render(renderContext);
    }
    
    function renderPages(pdfDoc) {
        for(var num = 1; num <= pdfDoc.numPages; num++)
            pdfDoc.getPage(num).then(renderPage);
    }
    PDFJS.disableWorker = true;
    PDFJS.getDocument(url).then(renderPages);
}   
</script> 

<div id="holder"></div>

<script type="text/javascript">
renderPDF('/files/adrin-jalali.pdf', document.getElementById('holder'));
</script>  
