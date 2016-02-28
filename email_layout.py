# Use this module for email subject
import datetime
# Interdependencies
from profiles import get_new_profiles, accounts

# Use this function to setup and format the email
def setup_email():
    # Html setup
    body = """
           <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
           <head><!-- NAME: SIMPLE TEXT --><!--[if gte mso 15]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
           <meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge">
           <meta name="viewport" content="width=device-width, initial-scale=1">
           """
    # Setup email subject
    today = datetime.date.today()
    email_subject = today.strftime('Weekly curated curiosity - %A %d, %b')
    body += "<title>" + email_subject + "</title>"

    # Style sheet and closing head tags
    body += """
               <style type="text/css">
            p{
                margin:10px 0;
                padding:0;
            }
            a{
                color:#2baadf;
            }
            table{
                border-collapse:collapse;
            }
            h1,h2,h3,h4,h5,h6{
                display:block;
                margin:0;
                padding:0;
            }
            img,a img{
                border:0;
                height:auto;
                outline:none;
                text-decoration:none;
            }
            body,#bodyTable,#bodyCell{
                height:100%;
                margin:0;
                padding:0;
                width:100%;
            }
            #outlook a{
                padding:0;
            }
            img{
                -ms-interpolation-mode:bicubic;
            }
            table{
                mso-table-lspace:0pt;
                mso-table-rspace:0pt;
            }
            .ReadMsgBody{
                width:100%;
            }
            .ExternalClass{
                width:100%;
            }
            p,a,li,td,blockquote{
                mso-line-height-rule:exactly;
            }
            a[href^=tel],a[href^=sms]{
                color:inherit;
                cursor:default;
                text-decoration:none;
            }
            p,a,li,td,body,table,blockquote{
                -ms-text-size-adjust:100%;
                -webkit-text-size-adjust:100%;
            }
            .ExternalClass,.ExternalClass p,.ExternalClass td,.ExternalClass div,.ExternalClass span,.ExternalClass font{
                line-height:100%;
            }
            a[x-apple-data-detectors]{
                color:inherit !important;
                text-decoration:none !important;
                font-size:inherit !important;
                font-family:inherit !important;
                font-weight:inherit !important;
                line-height:inherit !important;
            }
            #bodyCell{
                padding:10px;
            }
            .templateContainer{
                max-width:600px !important;
            }
            a.mcnButton{
                display:block;
            }
            .mcnImage{
                vertical-align:bottom;
            }
            .mcnTextContent{
                word-break:break-word;
            }
            .mcnTextContent img{
                height:auto !important;
            }
            .mcnDividerBlock{
                table-layout:fixed !important;
            }
            body,#bodyTable{
                background-color:#FFFFFF;
            }
            #bodyCell{
                border-top:0;
            }
            .templateContainer{
                border:0;
            }
            h1{
                color:#202020;
                font-family:Helvetica;
                font-size:26px;
                font-style:normal;
                font-weight:bold;
                line-height:125%;
                letter-spacing:normal;
                text-align:left;
            }
            h2{
                color:#202020;
                font-family:Helvetica;
                font-size:22px;
                font-style:normal;
                font-weight:bold;
                line-height:125%;
                letter-spacing:normal;
                text-align:left;
            }
            h3{
                color:#202020;
                font-family:Helvetica;
                font-size:20px;
                font-style:normal;
                font-weight:bold;
                line-height:125%;
                letter-spacing:normal;
                text-align:left;
            }
            h4{
                color:#202020;
                font-family:Helvetica;
                font-size:18px;
                font-style:normal;
                font-weight:bold;
                line-height:125%;
                letter-spacing:normal;
                text-align:left;
            }
            #templateHeader{
                border-top:0;
                border-bottom:0;
            }
            #templateHeader .mcnTextContent,#templateHeader .mcnTextContent p{
                color:#202020;
                font-family:Helvetica;
                font-size:16px;
                line-height:150%;
                text-align:left;
            }
            #templateHeader .mcnTextContent a,#templateHeader .mcnTextContent p a{
                color:#2BAADF;
                font-weight:normal;
                text-decoration:underline;
            }
            #templateBody{
                border-top:0;
                border-bottom:0;
            }
            #templateBody .mcnTextContent,#templateBody .mcnTextContent p{
                color:#202020;
                font-family:Helvetica;
                font-size:16px;
                line-height:150%;
                text-align:left;
            }
            #templateBody .mcnTextContent a,#templateBody .mcnTextContent p a{
                color:#2BAADF;
                font-weight:normal;
                text-decoration:underline;
            }
            #templateFooter{
                border-top:0;
                border-bottom:0;
            }
            #templateFooter .mcnTextContent,#templateFooter .mcnTextContent p{
                color:#202020;
                font-family:Helvetica;
                font-size:12px;
                line-height:150%;
                text-align:left;
            }
            #templateFooter .mcnTextContent a,#templateFooter .mcnTextContent p a{
                color:#202020;
                font-weight:normal;
                text-decoration:underline;
            }
            @media only screen and (min-width:768px){
                .templateContainer{
                    width:600px !important;
                }

            }	@media only screen and (max-width: 480px){
                    body,table,td,p,a,li,blockquote{
                        -webkit-text-size-adjust:none !important;
                    }

            }	@media only screen and (max-width: 480px){
                    body{
                        width:100% !important;
                        min-width:100% !important;
                    }

            }	@media only screen and (max-width: 480px){
                    #bodyCell{
                        padding-top:10px !important;
                    }

            }	@media only screen and (max-width: 480px){
                    .mcnImage{
                        width:100% !important;
                    }

            }	@media only screen and (max-width: 480px){
                    .mcnCaptionTopContent,.mcnCaptionBottomContent,.mcnTextContentContainer,.mcnBoxedTextContentContainer,.mcnImageGroupContentContainer,.mcnCaptionLeftTextContentContainer,.mcnCaptionRightTextContentContainer,.mcnCaptionLeftImageContentContainer,.mcnCaptionRightImageContentContainer,.mcnImageCardLeftTextContentContainer,.mcnImageCardRightTextContentContainer{
                        max-width:100% !important;
                        width:100% !important;
                    }

            }	@media only screen and (max-width: 480px){
                    .mcnBoxedTextContentContainer{
                        min-width:100% !important;
                    }

            }	@media only screen and (max-width: 480px){
                    .mcnImageGroupContent{
                        padding:9px !important;
                    }

            }	@media only screen and (max-width: 480px){
                    .mcnCaptionLeftContentOuter .mcnTextContent,.mcnCaptionRightContentOuter .mcnTextContent{
                        padding-top:9px !important;
                    }

            }	@media only screen and (max-width: 480px){
                    .mcnImageCardTopImageContent,.mcnCaptionBlockInner .mcnCaptionTopContent:last-child .mcnTextContent{
                        padding-top:18px !important;
                    }

            }	@media only screen and (max-width: 480px){
                    .mcnImageCardBottomImageContent{
                        padding-bottom:9px !important;
                    }

            }	@media only screen and (max-width: 480px){
                    .mcnImageGroupBlockInner{
                        padding-top:0 !important;
                        padding-bottom:0 !important;
                    }

            }	@media only screen and (max-width: 480px){
                    .mcnImageGroupBlockOuter{
                        padding-top:9px !important;
                        padding-bottom:9px !important;
                    }

            }	@media only screen and (max-width: 480px){
                    .mcnTextContent,.mcnBoxedTextContentColumn{
                        padding-right:18px !important;
                        padding-left:18px !important;
                    }

            }	@media only screen and (max-width: 480px){
                    .mcnImageCardLeftImageContent,.mcnImageCardRightImageContent{
                        padding-right:18px !important;
                        padding-bottom:0 !important;
                        padding-left:18px !important;
                    }

            }	@media only screen and (max-width: 480px){
                    .mcpreview-image-uploader{
                        display:none !important;
                        width:100% !important;
                    }

            }	@media only screen and (max-width: 480px){
                    h1{
                        font-size:22px !important;
                        line-height:125% !important;
                    }

            }	@media only screen and (max-width: 480px){
                    h2{
                        font-size:20px !important;
                        line-height:125% !important;
                    }

            }	@media only screen and (max-width: 480px){
                    h3{
                        font-size:18px !important;
                        line-height:125% !important;
                    }

            }	@media only screen and (max-width: 480px){
                    h4{
                        font-size:16px !important;
                        line-height:150% !important;
                    }

            }	@media only screen and (max-width: 480px){
                    table.mcnBoxedTextContentContainer td.mcnTextContent,td.mcnBoxedTextContentContainer td.mcnTextContent p{
                        font-size:14px !important;
                        line-height:150% !important;
                    }

            }	@media only screen and (max-width: 480px){
                    td#templateHeader td.mcnTextContent,td#templateHeader td.mcnTextContent p{
                        font-size:16px !important;
                        line-height:150% !important;
                    }

            }	@media only screen and (max-width: 480px){
                    td#templateBody td.mcnTextContent,td#templateBody td.mcnTextContent p{
                        font-size:16px !important;
                        line-height:150% !important;
                    }

            }	@media only screen and (max-width: 480px){
                    td#templateFooter td.mcnTextContent,td#templateFooter td.mcnTextContent p{
                        font-size:14px !important;
                        line-height:150% !important;
                    }

            }</style></head> """

    # Setup body html
    body += """
                 <body style="height: 100%;margin: 0;padding: 0;width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;background-color: #FFFFFF;">
                    <center>
                        <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;height: 100%;margin: 0;padding: 0;width: 100%;background-color: #FFFFFF;">
                            <tbody><tr>
                                <td align="left" valign="top" id="bodyCell" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;height: 100%;margin: 0;padding: 10px;width: 100%;border-top: 0;">
                                    <!-- BEGIN TEMPLATE // -->
                                    <!--[if gte mso 9]>
                                    <table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">
                                    <tr>
                                    <td align="center" valign="top" width="600" style="width:600px;">
                                    <![endif]-->
                                     <table border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border: 0;max-width: 600px !important;">
                                        <tbody>
            """
    # Section header
    body += """
            <tr>
                <td valign="top" id="templateHeader" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-top: 0;border-bottom: 0;">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width: 100%;border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
                        <tbody class="mcnTextBlockOuter">
                            <tr>
                                <td valign="top" class="mcnTextBlockInner" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
                                    <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width: 100%;border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;" class="mcnTextContentContainer">
                                    <tbody><tr>
                                        <td valign="top" class="mcnTextContent" style="padding-top: 19px;padding-right: 18px;padding-bottom: 9px;padding-left: 18px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;word-break: break-word;color: #202020;font-family: Helvetica;font-size: 16px;line-height: 150%;text-align: left;">
                                            <h1 style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 26px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">Tracking results</h1>
                                        </td>
                                    </tr></tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
            """
    # Tracking results section
    body += """
            <tr>
                <td valign="top" id="templateBody" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-top: 0;border-bottom: 0;">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width: 100%;border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
                        <tbody class="mcnTextBlockOuter">
                            <tr>
                                <td valign="top" class="mcnTextBlockInner" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
                                    <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width: 100%;border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;" class="mcnTextContentContainer">
                                        <tbody>
                                            <tr>
                                                <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-right: 18px;padding-bottom: 9px;padding-left: 18px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;word-break: break-word;color: #202020;font-family: Helvetica;font-size: 16px;line-height: 150%;text-align: left;">
                                                     <p style="margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-family: Helvetica;font-size: 16px;line-height: 150%;text-align: left;">
                                                        Hello Paul:
                                                     </p>
                                                     <p style="margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-family: Helvetica;font-size: 16px;line-height: 150%;text-align: left;">
                                                        I’ve found some interesting people worth checking out this week.
                                                     </p>
            """
    body += get_new_profiles(accounts)
    body += """
            <p style="margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-family: Helvetica;font-size: 16px;line-height: 150%;text-align: left;">
                Thanks for reading,
            </p>
            <p style="margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-family: Helvetica;font-size: 16px;line-height: 150%;text-align: left;">
                Hal,
            </p>
            """

    # Close out email
    body += """</td></tr></tbody></table></td></tr></tbody></table></td></tr>"""
    body += """</tbody></table><!--[if gte mso 9]></td></tr></table><![endif]--><!-- // END TEMPLATE --></td></tr></tbody></table></center></body></html>"""
    return body, email_subject


