import QRCode from 'qrcode';

export function createQRCode(canvasElement, url) {
    return QRCode.toCanvas(canvasElement, url, {
        width: 200,
        margin: 0,
	color: {
	    dark:"#1b2021",
	    light:"eaebed"
	}
    });    
}
