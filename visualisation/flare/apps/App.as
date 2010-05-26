package flare.apps
{
    import flash.display.Sprite;
    import flash.display.StageAlign;
    import flash.display.StageScaleMode;
    import flash.events.Event;
    import flash.geom.Rectangle;
    import flash.system.*;
    import flash.utils.*;
    
    import mx.core.*;
    import mx.resources.*;        
    
    public class App extends Sprite
    {        
        protected var _appBounds:Rectangle;
        
        public function App()
        {            
            addEventListener(Event.ADDED_TO_STAGE, onStageAdd);
        }        
        
        private function onStageAdd(evt:Event):void
        {
            removeEventListener(Event.ADDED_TO_STAGE, onStageAdd);
            initStage();
            //init();
            addEventListener("init_demo", init);
            onResize();
            stage.addEventListener(Event.RESIZE, onResize);
        }
        
        private function onResize(evt:Event=null):void
        {
            _appBounds = new Rectangle(0, 0, stage.stageWidth, stage.stageHeight);
            resize(_appBounds.clone());
        }
        
        protected function initStage():void
        {
            if (!stage) {
                throw new Error(
                    "Can't initialize Stage -- not yet added to stage");
            }
            stage.align = StageAlign.TOP_LEFT;
            stage.scaleMode = StageScaleMode.NO_SCALE;
        }
        
        protected function init(e:Event=null):void
        {
        }
        
        public function resize(bounds:Rectangle):void
        {
        }
        
    } // end of class App
}