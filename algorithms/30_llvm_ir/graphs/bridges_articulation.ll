; ModuleID = 'algorithms/02_c/graphs/bridges_articulation.c'
source_filename = "algorithms/02_c/graphs/bridges_articulation.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@timer = internal unnamed_addr global i32 0, align 4
@disc = internal unnamed_addr global [100 x i32] zeroinitializer, align 16
@parent = internal unnamed_addr global [100 x i32] zeroinitializer, align 16
@ap_flag = internal unnamed_addr global [100 x i32] zeroinitializer, align 16
@.str = private unnamed_addr constant [67 x i8] c"[C Bridges] FAILED: bridges=%d (want 1), articulation=%d (want 1)\0A\00", align 1
@low = internal unnamed_addr global [100 x i32] zeroinitializer, align 16
@str = private unnamed_addr constant [58 x i8] c"[C Bridges] Tarjan bridges + articulation points verified\00", align 1

; Function Attrs: nofree nosync nounwind sspstrong memory(readwrite, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local void @tarjan(ptr noundef readonly captures(none) %0, i32 noundef %1, ptr noundef captures(none) initializes((0, 4)) %2, ptr noundef captures(none) initializes((0, 4)) %3) local_unnamed_addr #0 {
  store i32 0, ptr @timer, align 4, !tbaa !5
  store i32 0, ptr %2, align 4, !tbaa !5
  store i32 0, ptr %3, align 4, !tbaa !5
  %5 = icmp sgt i32 %1, 0
  br i1 %5, label %6, label %10

6:                                                ; preds = %4
  %7 = zext nneg i32 %1 to i64
  %8 = shl nuw nsw i64 %7, 2
  tail call void @llvm.memset.p0.i64(ptr nonnull align 16 @disc, i8 0, i64 %8, i1 false), !tbaa !5
  tail call void @llvm.memset.p0.i64(ptr nonnull align 16 @parent, i8 -1, i64 %8, i1 false), !tbaa !5
  tail call void @llvm.memset.p0.i64(ptr nonnull align 16 @ap_flag, i8 0, i64 %8, i1 false), !tbaa !5
  %9 = zext nneg i32 %1 to i64
  br label %11

10:                                               ; preds = %18, %4
  ret void

11:                                               ; preds = %6, %18
  %12 = phi i64 [ 0, %6 ], [ %19, %18 ]
  %13 = getelementptr inbounds nuw i32, ptr @disc, i64 %12
  %14 = load i32, ptr %13, align 4, !tbaa !5
  %15 = icmp eq i32 %14, 0
  br i1 %15, label %16, label %18

16:                                               ; preds = %11
  %17 = trunc nuw nsw i64 %12 to i32
  tail call fastcc void @dfs(ptr noundef %0, i32 noundef %1, i32 noundef %17, ptr noundef nonnull %2, ptr noundef nonnull %3)
  br label %18

18:                                               ; preds = %11, %16
  %19 = add nuw nsw i64 %12, 1
  %20 = icmp eq i64 %19, %9
  br i1 %20, label %10, label %11, !llvm.loop !9
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nosync nounwind sspstrong memory(readwrite, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define internal fastcc void @dfs(ptr noundef readonly captures(none) %0, i32 noundef %1, i32 noundef %2, ptr noundef captures(none) %3, ptr noundef captures(none) %4) unnamed_addr #0 {
  %6 = load i32, ptr @timer, align 4, !tbaa !5
  %7 = add nsw i32 %6, 1
  store i32 %7, ptr @timer, align 4, !tbaa !5
  %8 = sext i32 %2 to i64
  %9 = getelementptr inbounds i32, ptr @low, i64 %8
  store i32 %7, ptr %9, align 4, !tbaa !5
  %10 = getelementptr inbounds i32, ptr @disc, i64 %8
  store i32 %7, ptr %10, align 4, !tbaa !5
  %11 = icmp sgt i32 %1, 0
  br i1 %11, label %12, label %17

12:                                               ; preds = %5
  %13 = getelementptr inbounds [100 x i32], ptr %0, i64 %8
  %14 = getelementptr inbounds i32, ptr @parent, i64 %8
  %15 = getelementptr inbounds i32, ptr @ap_flag, i64 %8
  %16 = zext nneg i32 %1 to i64
  br label %18

17:                                               ; preds = %74, %5
  ret void

18:                                               ; preds = %12, %74
  %19 = phi i32 [ %7, %12 ], [ %75, %74 ]
  %20 = phi i64 [ 0, %12 ], [ %77, %74 ]
  %21 = phi i32 [ 0, %12 ], [ %76, %74 ]
  %22 = getelementptr inbounds nuw i32, ptr %13, i64 %20
  %23 = load i32, ptr %22, align 4, !tbaa !5
  %24 = icmp eq i32 %23, 0
  br i1 %24, label %74, label %25

25:                                               ; preds = %18
  %26 = getelementptr inbounds nuw i32, ptr @disc, i64 %20
  %27 = load i32, ptr %26, align 4, !tbaa !5
  %28 = icmp eq i32 %27, 0
  br i1 %28, label %29, label %67

29:                                               ; preds = %25
  %30 = getelementptr inbounds nuw i32, ptr @parent, i64 %20
  store i32 %2, ptr %30, align 4, !tbaa !5
  %31 = add nsw i32 %21, 1
  %32 = trunc nuw nsw i64 %20 to i32
  tail call fastcc void @dfs(ptr noundef nonnull %0, i32 noundef %1, i32 noundef %32, ptr noundef %3, ptr noundef %4)
  %33 = getelementptr inbounds nuw i32, ptr @low, i64 %20
  %34 = load i32, ptr %33, align 4, !tbaa !5
  %35 = load i32, ptr %9, align 4, !tbaa !5
  %36 = icmp slt i32 %34, %35
  br i1 %36, label %37, label %39

37:                                               ; preds = %29
  store i32 %34, ptr %9, align 4, !tbaa !5
  %38 = load i32, ptr %33, align 4, !tbaa !5
  br label %39

39:                                               ; preds = %37, %29
  %40 = phi i32 [ %38, %37 ], [ %34, %29 ]
  %41 = phi i32 [ %34, %37 ], [ %35, %29 ]
  %42 = load i32, ptr %10, align 4, !tbaa !5
  %43 = icmp sgt i32 %40, %42
  br i1 %43, label %44, label %47

44:                                               ; preds = %39
  %45 = load i32, ptr %3, align 4, !tbaa !5
  %46 = add nsw i32 %45, 1
  store i32 %46, ptr %3, align 4, !tbaa !5
  br label %47

47:                                               ; preds = %44, %39
  %48 = load i32, ptr %14, align 4, !tbaa !5
  %49 = icmp eq i32 %48, -1
  %50 = icmp sgt i32 %21, 0
  %51 = select i1 %49, i1 %50, i1 false
  br i1 %51, label %52, label %58

52:                                               ; preds = %47
  %53 = load i32, ptr %15, align 4, !tbaa !5
  %54 = icmp eq i32 %53, 0
  br i1 %54, label %55, label %74

55:                                               ; preds = %52
  store i32 1, ptr %15, align 4, !tbaa !5
  %56 = load i32, ptr %4, align 4, !tbaa !5
  %57 = add nsw i32 %56, 1
  store i32 %57, ptr %4, align 4, !tbaa !5
  br label %74

58:                                               ; preds = %47
  %59 = icmp slt i32 %40, %42
  %60 = or i1 %59, %49
  br i1 %60, label %74, label %61

61:                                               ; preds = %58
  %62 = load i32, ptr %15, align 4, !tbaa !5
  %63 = icmp eq i32 %62, 0
  br i1 %63, label %64, label %74

64:                                               ; preds = %61
  store i32 1, ptr %15, align 4, !tbaa !5
  %65 = load i32, ptr %4, align 4, !tbaa !5
  %66 = add nsw i32 %65, 1
  store i32 %66, ptr %4, align 4, !tbaa !5
  br label %74

67:                                               ; preds = %25
  %68 = load i32, ptr %14, align 4, !tbaa !5
  %69 = zext i32 %68 to i64
  %70 = icmp ne i64 %20, %69
  %71 = icmp slt i32 %27, %19
  %72 = select i1 %70, i1 %71, i1 false
  br i1 %72, label %73, label %74

73:                                               ; preds = %67
  store i32 %27, ptr %9, align 4, !tbaa !5
  br label %74

74:                                               ; preds = %55, %52, %61, %64, %58, %73, %67, %18
  %75 = phi i32 [ %41, %61 ], [ %41, %64 ], [ %41, %55 ], [ %41, %58 ], [ %27, %73 ], [ %41, %52 ], [ %19, %67 ], [ %19, %18 ]
  %76 = phi i32 [ %31, %61 ], [ %31, %64 ], [ %31, %55 ], [ %31, %58 ], [ %21, %73 ], [ %31, %52 ], [ %21, %67 ], [ %21, %18 ]
  %77 = add nuw nsw i64 %20, 1
  %78 = icmp eq i64 %77, %16
  br i1 %78, label %17, label %18, !llvm.loop !11
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  %1 = alloca [100 x [100 x i32]], align 16
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #6
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(40000) %1, i8 0, i64 40000, i1 false)
  %4 = getelementptr inbounds nuw i8, ptr %1, i64 400
  store i32 1, ptr %4, align 16, !tbaa !5
  %5 = getelementptr inbounds nuw i8, ptr %1, i64 4
  store i32 1, ptr %5, align 4, !tbaa !5
  %6 = getelementptr inbounds nuw i8, ptr %1, i64 800
  %7 = getelementptr inbounds nuw i8, ptr %1, i64 804
  store i32 1, ptr %7, align 4, !tbaa !5
  %8 = getelementptr inbounds nuw i8, ptr %1, i64 408
  store i32 1, ptr %8, align 8, !tbaa !5
  %9 = getelementptr inbounds nuw i8, ptr %1, i64 8
  store i32 1, ptr %9, align 8, !tbaa !5
  store i32 1, ptr %6, align 16, !tbaa !5
  %10 = getelementptr inbounds nuw i8, ptr %1, i64 1208
  store i32 1, ptr %10, align 8, !tbaa !5
  %11 = getelementptr inbounds nuw i8, ptr %1, i64 812
  store i32 1, ptr %11, align 4, !tbaa !5
  call void @llvm.lifetime.start.p0(ptr nonnull %2) #6
  call void @llvm.lifetime.start.p0(ptr nonnull %3) #6
  store i32 0, ptr @timer, align 4, !tbaa !5
  store i32 0, ptr %2, align 4, !tbaa !5
  store i32 0, ptr %3, align 4, !tbaa !5
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(16) @disc, i8 0, i64 16, i1 false), !tbaa !5
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(16) @parent, i8 -1, i64 16, i1 false), !tbaa !5
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(16) @ap_flag, i8 0, i64 16, i1 false), !tbaa !5
  call fastcc void @dfs(ptr noundef nonnull readonly %1, i32 noundef 4, i32 noundef 0, ptr noundef nonnull %2, ptr noundef nonnull %3)
  %12 = load i32, ptr getelementptr inbounds nuw (i8, ptr @disc, i64 4), align 4, !tbaa !5
  %13 = icmp eq i32 %12, 0
  br i1 %13, label %14, label %15

14:                                               ; preds = %0
  call fastcc void @dfs(ptr noundef nonnull readonly %1, i32 noundef 4, i32 noundef 1, ptr noundef nonnull %2, ptr noundef nonnull %3)
  br label %15

15:                                               ; preds = %14, %0
  %16 = load i32, ptr getelementptr inbounds nuw (i8, ptr @disc, i64 8), align 8, !tbaa !5
  %17 = icmp eq i32 %16, 0
  br i1 %17, label %18, label %19

18:                                               ; preds = %15
  call fastcc void @dfs(ptr noundef nonnull readonly %1, i32 noundef 4, i32 noundef 2, ptr noundef nonnull %2, ptr noundef nonnull %3)
  br label %19

19:                                               ; preds = %18, %15
  %20 = load i32, ptr getelementptr inbounds nuw (i8, ptr @disc, i64 12), align 4, !tbaa !5
  %21 = icmp eq i32 %20, 0
  br i1 %21, label %22, label %23

22:                                               ; preds = %19
  call fastcc void @dfs(ptr noundef nonnull readonly %1, i32 noundef 4, i32 noundef 3, ptr noundef nonnull %2, ptr noundef nonnull %3)
  br label %23

23:                                               ; preds = %22, %19
  %24 = load i32, ptr %2, align 4, !tbaa !5
  %25 = icmp ne i32 %24, 1
  %26 = load i32, ptr %3, align 4
  %27 = icmp ne i32 %26, 1
  %28 = select i1 %25, i1 true, i1 %27
  br i1 %28, label %29, label %31

29:                                               ; preds = %23
  %30 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %24, i32 noundef %26)
  br label %33

31:                                               ; preds = %23
  %32 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  br label %33

33:                                               ; preds = %31, %29
  %34 = phi i32 [ 1, %29 ], [ 0, %31 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %3) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %2) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #6
  ret i32 %34
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #3

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #4

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #5

attributes #0 = { nofree nosync nounwind sspstrong memory(readwrite, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: write) }
attributes #4 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #5 = { nofree nounwind }
attributes #6 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
!11 = distinct !{!11, !10}
