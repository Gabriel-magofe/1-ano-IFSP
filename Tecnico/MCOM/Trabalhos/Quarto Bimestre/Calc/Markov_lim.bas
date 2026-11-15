'Function MARKOV_LIM(matriz As Variant) As Variant
'    Dim oScriptProvider As Object
'    oScriptProvider = ThisComponent.getScriptProvider()
'    
'    Dim sScriptURL As String
'    sScriptURL = "vnd.sun.star.script:PROB_LIM.py$MARKOV_PROB_LIM?" & _
'    "language=Python&location=user"
'    
'    ' 3. Carrega o script
'    Dim oScript As Object
'    oScript = oScriptProvider.getScript(sScriptURL)
'    
'    MARKOV_LIM = oScript.invoke(Array(matriz), Array(), Array())
'End Function

'professor, deste jeito que ensinou da erro com o getScriptProvider(), tentei resolver, vi que podia ser 
' que errei o nome do arquivo ou da função, mas não funcionou, joguei na ia, ela falou pra adicionar um .model antes
' disso que da erro mas não foi também, no fim esse abaixo foi o unico que funcionou.
Function MARKOV_LIM(matriz As Variant) As Variant
    Dim oDoc As Object
    Dim oScriptProvider As Object
    Dim oScript As Object
    Dim sScriptURL As String
    
    ' Pega o documento atual de forma segura
    oDoc = StarDesktop.getCurrentComponent()
    
    ' Verifica se o documento suporta provedor de scripts
    If Not IsNull(oDoc) And HasUnoInterfaces(oDoc, "com.sun.star.script.XScriptProviderSupplier") Then
        oScriptProvider = oDoc.getScriptProvider()
    Else
        ' Alternativa caso o contexto mude
        Dim oMasterScriptProviderFactory As Object
        oMasterScriptProviderFactory = CreateUnoService("com.sun.star.script.provider.MasterScriptProviderFactory")
        oScriptProvider = oMasterScriptProviderFactory.createScriptProvider("")
    End If
    
    ' Define o endereço do script Python
    sScriptURL = "vnd.sun.star.script:PROB_LIM.py$MARKOV_PROB_LIM?language=Python&location=user"
    
    ' Carrega e executa o script Python passando a matriz
    oScript = oScriptProvider.getScript(sScriptURL)
    MARKOV_LIM = oScript.invoke(Array(matriz), Array(), Array())
End Function